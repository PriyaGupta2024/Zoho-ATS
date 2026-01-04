1. Tech Stack
- Python 3.9
- Zoho Recruit REST API
- AWS Lambda (Serverless Framework)
- serverless-offline

2. Features
- Fetch open jobs from Zoho Recruit
- Create candidates
- Apply candidates to jobs
- List applications for a job
- OAuth token handling
- Clean standardized API

3.Setup Zoho Recruit Account
-Go to https://recruit.zoho.in
-Create a free trial account
-Choose Corporate HR account
-Create at least one Job Opening manually

4.Generate OAuth Token
-Create OAuth Client
-Go to: https://api-console.zoho.in/
-Client Type: Server-based
-Redirect URI: https://www.zoho.com
-Save your Client ID and Client Secret

5.Generate Authorization Code
Open in browser:
https://accounts.zoho.in/oauth/v2/auth?scope=ZohoRecruit.modules.ALL&client_id=YOUR_CLIENT_ID&response_type=code&access_type=offline&redirect_uri=https://www.zoho.com
Login and copy the code

6.Convert Code to Token
-POST https://accounts.zoho.in/oauth/v2/token
-Body (x-www-form-urlencoded):
grant_type=authorization_code
client_id=YOUR_CLIENT_ID
client_secret=YOUR_CLIENT_SECRET
redirect_uri=https://www.zoho.com
code=PASTE_CODE_HERE
-Save the refresh_token

7.Project Setup
Install
-npm install -g serverless
-npm install
-pip install requests

8.Environment Variables
Windows PowerShell:
setx ZOHO_REFRESH "your_refresh_token"
setx CLIENT_ID "your_client_id"
setx CLIENT_SECRET "your_client_secret"


9.Run Locally
serverless offline
Base URL:
http://localhost:3000/dev

10.API Endpoints
-GET /jobs
http://localhost:3000/dev/jobs
-POST /candidate
http://localhost:3000/dev/candidates
-GET /applications?job_id=...
http://localhost:3000/dev/applications?job_id=JOB_ID

