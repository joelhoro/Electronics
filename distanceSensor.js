const Gpio = require('pigpio').Gpio;
 
// The number of microseconds it takes sound to travel 1cm at 20 degrees celcius

var MICROSECONDS_PER_CM = 1e6/34321;
class DistanceSensor {

  constructor(triggerPort, echoPort) {
    this.trigger = new Gpio(triggerPort, {mode: Gpio.OUTPUT});
    this.echo = new Gpio(echoPort, {mode: Gpio.INPUT, alert: true});
    this.trigger.digitalWrite(0); // Make sure trigger is low
  }

  start(interval, callback) {
    let startTick;
    clearInterval(this.interval);

    this.echo.on('alert', (level, tick) => {
      if (level == 1) {
        startTick = tick;
      } else {
        const endTick = tick;
        const diff = (endTick >> 0) - (startTick >> 0); // Unsigned 32 bit arithmetic
        var distance = diff / 2 / MICROSECONDS_PER_CM;
        callback(distance);
      }
    });

    // Trigger a distance measurement once per interval
    this.interval = setInterval(() => {
      //  console.log("Sending signal")
        this.trigger.trigger(10, 1); // Set trigger high for 10 microseconds
      }, interval);
  }
}


exports.DistanceSensor = DistanceSensor;