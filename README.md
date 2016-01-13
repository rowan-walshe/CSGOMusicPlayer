# CSGOMusicPlayer

Uses CSGO's game state integration to play when you are dead, and pause it when you are alive. It should work with any application where you are able to control music with the play/pause button on your keyboard

To use place the gamestate integration file in the following folder

	\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\cfg\

If you are unable to find this folder than right click the game in steam, go to properties, local files and click local files.

Next change the steamid on line 29 of main.py to your steamid.

Run main.py

Things you may need to do
	
	download and install python 3
	
	install PyAutoGUI
		pip install PyAutoGUI
		This may through an error when installing. I fixed this by install Pillow (pip install Pillow)
	
	install requests as it is not included with python 3 by default
		pip install requests
	
Known issues
	
	If you are using spotify and an advert is playing when your state changes then it won't play/pause the music when it stops
		Fixes:
			Play/pause the music when the advert has finished
			Pay for spotify premium so there are no adds

Any input is greatly appreciated. It is very basic, as I just through it together, while learning python at the same time.

I will continue to update it as I learn more and think of features to add