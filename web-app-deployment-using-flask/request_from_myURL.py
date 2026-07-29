"""this module is used to request from my url"""
import requests

myURL=requests.get("http://127.0.0.1:5000/")
print(myURL.status_code)
print(myURL.server)