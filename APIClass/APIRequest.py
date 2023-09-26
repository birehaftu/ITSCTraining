import requests
#url="http://127.0.0.1:8000/my-second-api?name=birhane "
url="http://127.0.0.1:8000/my-getdata-api"
response=requests.get(url)
##try:
#print(response.content)#display content
print(response.json())#display json
##catch