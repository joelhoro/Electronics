var StartServer = require('./server');
var Servo = require('./servo');

// connect yellow wire with pin 4 (#7)
// red to 5V / black to ground
const gpio_ports = [4,18,23,24];
const motors = gpio_ports.map(gpio_port => new Servo(gpio_port));
var positions = [50,34,31,50];
initializePositions();


function initializePositions() {
    [0,1,2,3].map(idx => setPositions(idx, positions[idx]));
}

function setPositions(idx,value) {
    var servo = motors[idx];
    servo.setAngle(value);
    io.emit('positions', {idx, position: value});
}


var positionsMessage;

StartServer(3000, function(socket) { 
    initializePositions();
    socket.on('positions', function(data) {
        console.log(">>> ", data);
        var idx = data.idx;
        var position = data.position;
        clearTimeout(positionsMessage);
        positionsMessage = setTimeout(() => {
            console.log("Setting pulse to ", data);
        }, 100 );
        setPositions(idx,position);
    });
})
