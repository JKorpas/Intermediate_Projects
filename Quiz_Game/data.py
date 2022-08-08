import requests

response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
if response.ok == True:
    question_data = response.json()["results"]
