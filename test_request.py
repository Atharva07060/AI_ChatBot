import requests

url = "http://localhost:5000/chat"
payload = {"message": "I want a refund"}
response = requests.post(url, json=payload)

print(response.json())
