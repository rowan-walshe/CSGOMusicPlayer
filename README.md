# CSGOMusicPlayer

Uses CSGO's game state integration to play when you are dead, and pause it when you are alive. It should work with any application where you are able to control music with the play/pause button on your keyboard


### Installation

#### Windows

Place the gamestate integration file in the following folder

	\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\cfg\

In command prompt navigate to the CSGO you downloaded the project to. This will most likely be in downloads. You can navigate to the folder using the cd command. Below will what you have to type if you saved the file to Downloads.

	cd Downloads

	cd CSGOMusicPlayer

Next run the following command

	pip install -r requirements-windows.txt

If it gives an error like pip is not recognised, make sure you have python 3 installed, or trying using pip3 instead of pip

Next open main.py in a text editor. On line 25 where it says the line below, and change the number to your steamid. If you need to find out what yours is go to https://steamcommunity.com, login and click on your profile picture in the top right. You steamid will be the number that it shows in the address bar.

	if steamid == '76561198058071054':

Save the file, and then in the command promt window again, run

	python main.py

If it doesn't work try

	python3 main.py

#### OSX

The only differences from the windows intructions are that PyAutoGUI has more dependences. I will add a more instructions tomorrow as it is currently 6 in the morning

#### Linux

The only differences from the windows intructions are that PyAutoGUI has more dependences. I will add a more instructions tomorrow as it is currently 6 in the morning
	
#### Known issues
	
1. If you are using spotify and an advert is playing when your state changes then sometimes it won't play/pause the music when it stops
..*Play/pause the music when the advert has finished
..*Pay for spotify premium so there are no adds

Any input is greatly appreciated. It is very basic, as I just through it together, while learning python at the same time.

I will continue to update it as I learn more and think of features to add
