import requests

url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"

headers = {
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com",
        "X-RapidAPI-Key": "e3a99613d0msh76852b910eda6d4p1e0758jsneef3fa74db48"  # Replace with your RapidAPI key
    }
response = requests.get(url, headers=headers)
print(response.json())
  
