var i2cBus = require("i2c-bus");
var Pca9685Driver = require("pca9685").Pca9685Driver;
 
var options = {
    i2c: i2cBus.openSync(1),
    address: 0x40,
    frequency: 50,
    debug: false
};

pwm = new Pca9685Driver(options, function(err) {
    if (err) {
        console.error("Error initializing PCA9685");
        process.exit(-1);
    }
    console.log("Initialization done"); 
//    pwm.setPulseLength(2, 1500);
});



var pulseWidth_min = 500
var pulseWidth_max = 2450

function timer(ms) {
    return new Promise(res => setTimeout(res, ms));
}

class Servo {
    constructor(channel, initialAngle) {
        this.channel = channel;
        // this.motor = new Gpio(gpio_port, {mode: Gpio.OUTPUT });
        // this.motor.pwmFrequency(50);
        this.setAngle(initialAngle);
    }

    setAngle(angle) {
        this.angle = angle;
        console.log("Setting angle to ", this.angle);
        angle = Math.min(180,Math.max(0,angle));
        var dutyCycle = 0.02 + (angle/180) * 0.1;
        pwm.setDutyCycle(this.channel,dutyCycle)
    }
    async goToAngle(angle, interval) {
        var diff = angle - this.angle;
        var steps = Math.min(100.0, diff);
        if(interval<50)
            steps = 1;
        for(var i = 0; i < steps; i++) {
            this.setAngle(this.angle + diff / steps);
            await timer(interval/steps);
        }
    }

    demo(steps = 10) {
        // var i = 0;
        // var angle = 0;
        // var step = 45;
        // var interval = 100 * step/10;

        // var move = () => {
        //     i++;
        //     if(angle > 180 || angle < 0)
        //         step *= -1
        //     angle += step;
        //     this.setAngle(angle);
        //     console.log(i);
        //     if(i<steps) {
        //         console.log(i,": repeating");
        //         setTimeout(move, interval);
        //     }
        // };

        // move();
        this.setAngle(0);
        setTimeout(() => this.setAngle(180),500);
        setTimeout(() => this.setAngle(0),1000);
    }
}

exports.Servo = Servo;

