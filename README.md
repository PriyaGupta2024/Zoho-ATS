# 🚀 Zoho ATS Integration Microservice

A lightweight Applicant Tracking System (ATS) Integration Microservice built using Python + AWS Lambda (Serverless Framework) that connects with Zoho Recruit and exposes a unified REST API.

---

## 🛠 Tech Stack
- Python 3.9  
- Zoho Recruit REST API  
- AWS Lambda  
- Serverless Framework  
- serverless-offline  

---

## ✨ Features
- Fetch open jobs from Zoho Recruit  
- Create candidates  
- Apply candidates to job openings  
- List applications for a job  
- OAuth token handling  
- Clean standardized API  

---

## 🧑‍💼 Setup Zoho Recruit Account
1. Go to https://recruit.zoho.in  
2. Create a free trial account  
3. Choose Corporate HR account  
4. Create at least one Job Opening  

---

## 🔐 Generate OAuth Credentials

### Step 1 – Create OAuth Client  
Go to https://api-console.zoho.in  
- Client Type: Server-based  
- Redirect URI:  
  https://www.zoho.com  

Save your Client ID & Client Secret.

---

### Step 2 – Generate Authorization Code

Open in browser:

https://accounts.zoho.in/oauth/v2/auth?scope=ZohoRecruit.modules.ALL&client_id=YOUR_CLIENT_ID&response_type=code&access_type=offline&redirect_uri=https://www.zoho.com

Copy the `code` from redirected URL.

---

### Step 3 – Convert Code to Token

POST  
https://accounts.zoho.in/oauth/v2/token  

Body (x-www-form-urlencoded):

grant_type=authorization_code  
client_id=YOUR_CLIENT_ID  
client_secret=YOUR_CLIENT_SECRET  
redirect_uri=https://www.zoho.com  
code=PASTE_CODE_HERE  

Save the `refresh_token`.

---

## ⚙ Project Setup

Install dependencies:
npm install -g serverless
npm install
pip install requests

---

## 🌱 Environment Variables (Windows)
setx ZOHO_REFRESH "your_refresh_token"
setx CLIENT_ID "your_client_id"
setx CLIENT_SECRET "your_client_secret"

Restart terminal after setting.

---

## ▶ Run Locally

Base URL:
http://localhost:3000/dev

---

## 🔌 API Endpoints

### GET /jobs
http://localhost:3000/dev/jobs

---

### POST /candidates
http://localhost:3000/dev/candidates

Body:
{
"name": "John Doe",
"email": "john@example.com",
"phone": "9876543210",
"job_id": "JOB_ID"
}


---

### GET /applications?job_id=JOB_ID
http://localhost:3000/dev/applications?job_id=JOB_ID
