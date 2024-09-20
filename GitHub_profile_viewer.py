import requests

token = "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"
#url=("https://github.com/alihussien07")
username = "alihussien07"
url = f"https://api.github.com/users/{username}"
response=requests.get(url)
if response.status_code == 200:
    user_data = response.json()
    print(f"User: {user_data['login']}")
    print(f"Name: {user_data.get('name', 'No name available')}")
    print(f"Bio: {user_data.get('bio', 'No bio available')}")
    print(f"Public Repositories: {user_data['public_repos']}")
    print(f"Followers: {user_data['followers']}")
    print(f"Following: {user_data['following']}")

else:
    print(f"Failed to retrieve data: {response.status_code}")
