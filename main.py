import pyautogui
import logging
from flask import Flask, request, g

TARGET_STEAM_ID = '76561198058071054'

# stops the app printing to console unless there is an error
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)


@app.route("/", methods=["POST"])
def main():
    previous_health = g.get('previous_health', 100)

    # Imports the json information and stores player information
    player = request.json.get('player', {})

    # Steamid of the player that is using the app. This stops the health that is read in from showing someone elses health when you are dead
    if player.get('steamid', None) == TARGET_STEAM_ID:
        # If the steamid is correct then it extracts the information about the players health fromt he json
        player_state = player.get('state', {})
        health = player_state.get('health', None)

        # If the player goes from being alive to dead or vice versa then it plays/pauses the music using the windows media key play/pause
        if health == 0 and previous_health != 0:
            pyautogui.press('playpause')
        elif health != 0 and previous_health == 0:
            pyautogui.press('playpause')
        if health:
            g.previous_health = health
    return 'OK', 200


if __name__ == "__main__":
    print('Running')
    app.run(port=3000)
