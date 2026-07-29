"""this module is used to request from my url"""
import requests

get_request=requests.get("http://127.0.0.1:5000/")
print(get_request.status_code)
post_response = requests.post("http://127.0.0.1:5000/health")
print("POST Response:", post_response.json())
