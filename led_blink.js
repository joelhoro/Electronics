const path = require('path');
const Gpio = require('pigpio').Gpio;

const express = require('express')
const app = express()
const port = 3000

var http = require('http').Server(app);
var io = require('socket.io')(http);

const gpio_port = 4;

const led = new Gpio(gpio_port, {mode: Gpio.OUTPUT});

app.use('/', express.static(path.resolve(__dirname)))

io.on('connection', function(socket) {

    socket.on('brightness', function(value) {
        led.pwmWrite(value);
    });

})

http.listen(port, () => console.log(`Example app listening on port ${port}!`))