const Gpio = require('pigpio').Gpio;

var pulseWidth_min = 500
var pulseWidth_max = 2450

class Servo {
    constructor(gpio_port) {
        this.motor = new Gpio(gpio_port, {mode: Gpio.OUTPUT });
        this.motor.pwmFrequency(50);
    }

    setAngle(angle) {
        this.angle = angle;
        console.log(positions);
        console.log("Setting ", idx, " to ", angle);
        angle = Math.min(180,Math.max(0,angle));
        var pulseWidth = pulseWidth_min + (pulseWidth_max-pulseWidth_min) / 180.0 * angle;
        pulseWidth = Math.round(pulseWidth)
        console.log("Emitting: ", angle, pulseWidth)
        this.motor.servoWrite(pulseWidth);
    }
}

exports.Servo = Servo;
