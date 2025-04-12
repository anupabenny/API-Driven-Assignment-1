# URL - https://app.prefect.cloud/account/8ff8f613-92c4-44ce-b811-f9956023e78d/workspace/04d8fca9-df2e-40c8-ae4f-a3733114c475/dashboard

# URL - https://app.prefect.cloud/api/docs

import requests

# Replace these variables with your actual Prefect Cloud credentials
PREFECT_API_KEY = "pnu_XljdzRwZJ4iz1d4KjVl00YdMmKtQ230qS2Bi"  # Your Prefect Cloud API key
ACCOUNT_ID = "37329c1a-59cd-4359-87ff-ac4004fb0fa4"  # Your Prefect Cloud Account ID
WORKSPACE_ID = "d927089c-f4ed-4ac3-9498-dd2b58613b75"  # Your Prefect Cloud Workspace ID
FLOW_ID = "6e8f1fe9-9c71-48fb-bd35-7c8d18f4f14d"  # Your Flow ID for workflow.py

# Correct API URL to get flow details
PREFECT_API_URL = f"https://api.prefect.cloud/api/accounts/{ACCOUNT_ID}/workspaces/{WORKSPACE_ID}/flows/{FLOW_ID}"

# Set up headers with Authorization
headers = {"Authorization": f"Bearer {PREFECT_API_KEY}"}

# Make the request using GET
response = requests.get(PREFECT_API_URL, headers=headers)

# Check the response status
if response.status_code == 200:
    flow_info = response.json()
    print(flow_info)
else:
    print(f"Error: Received status code {response.status_code}")
    print(f"Response content: {response.text}")
