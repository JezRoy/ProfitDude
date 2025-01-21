import sys
import requests

apiKey = "" # Needs to be inputted
urlBase = f"https://api.rawg.io/api/"

def searchGame(name):
    """Search for a game by name."""
    urlQuery = f"{urlBase}/games?key={apiKey}&search={name}"
    response = requests.get(urlQuery)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}
    
def getGameData(slugName):
    """Get detailed information about a game."""
    urlQuery = f"{urlBase}/games/{slugName}?key={apiKey}"
    response = requests.get(urlQuery)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}