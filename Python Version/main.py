import pyautogui
import logging
import json
from time import sleep
from flask import Flask, request



log = logging.getLogger('werkzeug')
log.setLevel(logging.INFO)

state = 'PlayMusic'
lastCheck = 'PlayMusic'
#Insert SteamID Here
mySteamID = '34432432'
#Change deathDelay if you want to hear footsteps etc...
deathDelay = 3
app = Flask(__name__)

@app.route("/", methods=["POST"])
def main():

    global state
    global lastCheck
    global deathDelay
    
    player = request.json.get('player', {})
    round = request.json.get('round', {})
    
    if player['steamid'] != mySteamID or player['state']['health'] == 0 or round['phase'] in ('freezetime','warmup','over'):
        lastCheck = 'PlayMusic'
    else:
        lastCheck = 'StopPlaying'

    if lastCheck == 'PlayMusic' and state == 'StopPlaying':
        print(lastCheck)
        sleep(deathDelay)
        pyautogui.press('playpause')
        state = lastCheck
    elif lastCheck != state:
        print(lastCheck)
        pyautogui.press('playpause')
        state = lastCheck
        
        
if __name__ == "__main__":
    print('Running')
    app.run(port=3000)
