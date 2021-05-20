import requests

request = requests.get("https://yts.mx/api/v2/movie_details.json?movie_id=24")
response = request.json()
print(response['data']['movie']['genres'])