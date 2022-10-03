import requests

parameters = {
    "amount": 5,
    "type": "boolean",
    #"category": "21",

}

response = requests.get("https://opentdb.com/api.php", params=parameters)
if response.ok == True:
    question_data = response.json()["results"]
