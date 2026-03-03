import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

print("First Post:")
print("Title:", data[0]["title"])
print("Body:", data[0]["body"])