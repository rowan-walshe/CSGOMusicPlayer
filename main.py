import json
import requests
from flask import Flask, session, request, current_app

previous_health = 0

app = Flask(__name__)

@app.route("/", methods=["POST"])
def main():
	json_data = json.loads(request.data)
	player = json_data.get('player', {})
	steamid = player.get('steamid', '')
	if steamid == '76561198058071054':
		player_state = player.get('state', '')
		health = int(player_state.get('health', ''))
		if health == 0 and previous_health != 0:
			# TODO play music
			print 'dead'
		elif health != 0 and previous_health == 0:
			# TODO pause music
			print 'alive'
		global previous_health
		previous_health = health
		# print request.data
	return ''

if __name__ == "__main__":
	app.run(port=3000, debug=True)