http = require('http')
robot = require('robotjs')

port = 3000
host = '127.0.0.1'
previous_health = 0

server = http.createServer( function(req, res) {

    if (req.method == 'POST') {
        
        res.writeHead(200, {'Content-Type': 'text/html'})

        var body=''
        req.on('error', function(err) {
            console.error(err)
        }).on('data', function (data) {
            body += data
        }).on('end', function () {
            res.end( '' )
            parsePlayerUpdate(JSON.parse(body))
        })  
    }

}).listen(port, host)

// Takes the parsed json and plays/pauses the music when it should
function parsePlayerUpdate(update) {
    
    steamid = update.player.steamid
    activity = update.player.activity

    if(steamid == '76561198058071054' && activity !== 'menu') {
        try {
            health = update.player.state.health
            if((health > 0 && previous_health == 0) || (health == 0 && previous_health > 0)) {
                robot.keyTap('audio_pause')
                console.log('play/pause')
            }

            previous_health = update.player.state.health
        } catch(err) {
            console.error(err)
        }
    }
}

console.log('Listening at http://' + host + ':' + port)