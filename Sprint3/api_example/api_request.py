import requests

request = requests.get("https://lambda-ds-twit-assist.herokuapp.com/user/bindureddy")
ditto_pydict = request.json()
print(ditto_pydict['twitter_handle']['username'])