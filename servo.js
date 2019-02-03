const path = require('path');
const Gpio = require('pigpio').Gpio;

const express = require('express');
const app = express();
const port = 3000;

var http = require('http').Server(app);
var io = require('socket.io')(http);

const gpio_port = 4;

const motor = new Gpio(gpio_port, {mode: Gpio.OUTPUT});
motor.pwmFrequency(50)

var pulseWidth_min = 500
var pulseWidth_max = 2450
let pulseWidth = pulseWidth_min;
let increment_base = 10;
var increment = increment_base;

// setInterval(() => {
//   motor.servoWrite(pulseWidth);

// //  console.log(pulseWidth);
//   pulseWidth += increment;
//   if (pulseWidth > pulseWidth_max) {
//     increment = -increment_base;
//   } else if (pulseWidth < pulseWidth_min) {
//     increment = increment_base;
//   }
// }, 10);

setBrightness(0);

function setBrightness(value) {
    value = Math.min(100,Math.max(0,value));
    var pulseWidth = pulseWidth_min + (pulseWidth_max-pulseWidth_min) / 100.0 * value;
    pulseWidth = Math.round(pulseWidth)
    console.log(value, pulseWidth)
    motor.servoWrite(pulseWidth);
}

app.use('/', express.static(path.resolve(__dirname)))

var brightnessMessage;

io.on('connection', function(socket) { 

    socket.on('brightness', function(value) {
        clearTimeout(brightnessMessage);
        brightnessMessage = setTimeout(() => {
            console.log("Setting pulse to to ", value);
            io.emit('brightness', value);
        }, 100 );
        setBrightness(value);
    });

})

http.listen(port, () => console.log(`Example app listening on port ${port}!`))
