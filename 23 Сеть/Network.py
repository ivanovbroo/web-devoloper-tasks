import requests
import json
import pickle

URL = "https://webhook.site/241a0acb-b733-42c1-a4ee-15d054e27355"

users = requests.get("https://jsonplaceholder.typicode.com/users")
comments = requests.get("https://jsonplaceholder.typicode.com/comments")
posts = requests.get("https://jsonplaceholder.typicode.com/posts")

statistics = [{"id": user["id"],
                "username": user["username"],
                "email": user["email"],
                "posts": sum([1 for post in posts.json() if post["userId"] == user["id"]]),
                "comments": sum([1 for comment in comments.json() if comment["email"] == user["email"]])}
                for user in users.json()]

response = requests.post(URL, data = json.dumps({"statistics": statistics}))

with open("result.pickle", mode="wb") as f:
    pickle.dump(response, f)
