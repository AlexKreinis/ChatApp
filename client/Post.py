import requests
import sys


print("started2")
URL = "http://localhost:5000/api/chat"
try:
    msg = sys.argv[1]
except:
    msg = 'test msg2'

PARAMS = {'ID': "testUser", "otherID": "testUser2", 'chat': {"senderName": "testUser", "text": msg}}

r = requests.post(url=URL, json=PARAMS)#sending data to the server
pastebin_url = r.text
print("now get")

URL = "http://localhost:5000/api/chat/99/87"


ans = requests.get(url=URL)
data = r.json() 
print("and the answer is :\n")
print(data)


