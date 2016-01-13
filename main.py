import json
import requests
import pyautogui
import logging
from flask import Flask, session, request, current_app

# stops the app printing to console unlese there is an error
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# VK_MEDIA_PLAY_PAUSE = 0xB3
# hwcode = win32api.MapVirtualKey(VK_MEDIA_PLAY_PAUSE, 0)

previous_health = 100

app = Flask(__name__)

@app.route("/", methods=["POST"])
def main():
	global previous_health
	
	# Imports the json information and stores player information
	json_data = json.loads(request.data.decode())
	player = json_data.get('player', {})
	steamid = player.get('steamid', '')

	# Steamid of the player that is using the app. This stops the health that is read in from showing someone elses health when you are dead
	if steamid == '76561198058071054':

		#If the steamid is correct then it extracts the information about the players health fromt he json
		player_state = player.get('state', '')
		health = int(player_state.get('health', ''))

		# If the player goes from being alive to dead or vice versa then it plays/pauses the music using the windows media key play/pause
		if health == 0 and previous_health != 0:
			pyautogui.press('playpause')
		elif health != 0 and previous_health == 0:
			pyautogui.press('playpause')
		previous_health = health
	return 'you lost the game'

if __name__ == "__main__":
	print('Running')
	app.run(port=3000)