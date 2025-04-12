import requests

# Replace these variables with your actual Prefect Cloud credentials
PREFECT_API_KEY = "pnu_XljdzRwZJ4iz1d4KjVl00YdMmKtQ230qS2Bi"  # Your Prefect Cloud API key
ACCOUNT_ID = "37329c1a-59cd-4359-87ff-ac4004fb0fa4"  # Your Prefect Cloud Account ID
WORKSPACE_ID = "d927089c-f4ed-4ac3-9498-dd2b58613b75"  # Your Prefect Cloud Workspace ID
DEPLOYMENT_ID = "601c0a87-f0db-4e23-a83e-0e066c148243"  # workflow.py deployment

# Correct API URL to get deployment details
PREFECT_API_URL = f"https://api.prefect.cloud/api/accounts/{ACCOUNT_ID}/workspaces/{WORKSPACE_ID}/deployments/{DEPLOYMENT_ID}"

# Set up headers with Authorization
headers = {"Authorization": f"Bearer {PREFECT_API_KEY}"}

# Make the request using GET
response = requests.get(PREFECT_API_URL, headers=headers)

# Check the response status
if response.status_code == 200:
    deployment_info = response.json()
    print(deployment_info)
else:
    print(f"Error: Received status code {response.status_code}")
    print(f"Response content: {response.text}")
