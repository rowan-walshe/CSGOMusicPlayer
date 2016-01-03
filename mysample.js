// "CSGO Music Player v0.1" server
var http = require('http');
var fs = require('fs');

var bodyParser = require('body-parser');
var express = require('express');
var app = express();

var port = 3000;
var host = '127.0.0.1';

var previousHealth = 0;

app.post('/', function(req, res) {
	var round = 'round' in req.body ? req.body.round : null;
	var health = 'health' in req.body.player.state ? req.body.player : null;
	if(health == 0) {
		// TODO start music
	} else {
		// TODO stop music
	}
	console.log(health);
	  fs.writeFile('bomb_status', newBombStatus);
	  console.log(newBombStatus);
});

server = http.createServer( function(req, res) {
 
	if (req.method == 'POST') {
		res.writeHead(200, {'Content-Type': 'text/html'});
 
		var body = '';
		var health = 'health' in req.body.player.state ? req.body.player : null;
		previousHealth = health;
		if(health == 0 && previousHealth == 0) {
			console.log("Alive.");
		} else if(changedState && previousHealth > 0){
			console.log("Dead.");
		}
	} else {
		console.log("Not expecting other request types...");
		res.writeHead(200, {'Content-Type': 'text/html'});
		var html = '<html><body>HTTP Server at http://' + host + ':' + port + '</body></html>';
		res.end(html);
	}
}).listen(port, host);

console.log('Listening at http://${hostname}:${port}/');
