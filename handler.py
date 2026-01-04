import json, os, requests

# Your Recruit Org ID (from your URL)
ORG_ID = "60062870724"

# Zoho Recruit ATS API Base (India DC)
BASE = "https://recruit.zoho.in/recruit/v2"


def get_token():
    r = requests.post("https://accounts.zoho.in/oauth/v2/token", data={
        "refresh_token": os.environ['ZOHO_REFRESH'],
        "client_id": os.environ['CLIENT_ID'],
        "client_secret": os.environ['CLIENT_SECRET'],
        "grant_type": "refresh_token"
    }, timeout=10)

    return r.json()["access_token"]


def call_recruit(path, method="get", payload=None):
    token = get_token()

    headers = {
        "Authorization": f"Zoho-oauthtoken {token}",
        "X-CRM-ORG-ID": ORG_ID,
        "Content-Type": "application/json"
    }

    url = f"{BASE}/{path}"
    r = requests.request(method, url, headers=headers, json=payload, timeout=15)

    return r


# GET ALL JOBS
def get_jobs(event, context):
    r = call_recruit("JobOpenings")
    return {"statusCode": 200, "body": r.text}


# CREATE CANDIDATE
def create_candidate(event, context):
    data = json.loads(event["body"])

    payload = {
        "data": [{
            "First_Name": data["name"],
            "Last_Name": "Auto",
            "Email": data["email"],
            "Phone": data["phone"]
        }]
    }

    r = call_recruit("Candidates", "post", payload)
    return {"statusCode": 200, "body": r.text}


# GET APPLICATIONS
# GET /applications?job_id=...
def list_applications(event, context):
    params = event.get("queryStringParameters") or {}
    job_id = params.get("job_id")

    if not job_id:
        return {"statusCode":400,"body":json.dumps({"error":"job_id required"})}

    r = call_recruit(
        f"Applications/search?criteria=(Job_Opening:equals:{job_id})"
    )

    raw = r.json().get("data", [])

    result = []
    for a in raw:
        result.append({
            "id": a.get("id"),
            "candidate_name": a.get("Candidate_Name", {}).get("name"),
            "email": a.get("Email"),
            "status": a.get("Application_Status", "APPLIED")
        })

    return {"statusCode":200,"body":json.dumps(result)}


    
def apply_candidate(event, context):
    data = json.loads(event["body"])

    payload = {
        "data": [{
            "Job_Opening_Id": data["job_id"]
        }]
    }

    r = call_recruit(f"Candidates/{data['candidate_id']}/associate", "post", payload)

    return {"statusCode": 200, "body": r.text}


    
    
