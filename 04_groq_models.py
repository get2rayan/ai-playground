import requests
import os
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv()

api_key = os.environ.get('GROQ_API_KEY')
url = "https://api.groq.com/openai/v1/models"

# print(f"api_key : {api_key}")
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

response = requests.get(url=url, headers=headers)
pretty_json = json.dumps(response.json(), indent=2)
print(pretty_json)