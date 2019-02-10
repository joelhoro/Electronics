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
});

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
        this.setAngle(0);
        setTimeout(() => this.setAngle(180),500);
        setTimeout(() => this.setAngle(0),1000);
    }
}

exports.Servo = Servo;