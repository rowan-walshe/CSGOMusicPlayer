import pyautogui
import logging
import json
from flask import Flask, request

TARGET_STEAM_ID = '76561198058071054'

# Stops the app from printing to console unless there is an error
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

previous_health = 100

app = Flask(__name__)


@app.route("/", methods=["POST"])
def main():

    global previous_health

    # Imports the json information and stores player information
    player = request.json.get('player', {})

    # Steamid of the player that is using the app. This stops the health that is read in from showing someone elses health when you are dead
    if player.get('steamid', None) == TARGET_STEAM_ID:
        # If the steamid is correct then it extracts the information about the players health fromt he json
        player_state = player.get('state', {})
        health = player_state.get('health', None)

        # If the player goes from being alive to dead or vice versa then it plays/pauses the music using the windows media key play/pause4
        if health == 0 and previous_health != 0:
            pyautogui.press('playpause')
            # print("Died")
        elif health != 0 and previous_health == 0:
            pyautogui.press('playpause')
            # print("Alive")
        previous_health = health
    return ("", 200)


if __name__ == "__main__":
    print('Running')
    app.run(port=3000)
