var StartServer = require('./server').StartServer;
var Servo = require('./servo2').Servo;

// connect yellow wire with pin 4 (#7)
// red to 5V / black to ground
//const gpio_ports = [4,18,23,24];
//const motors = gpio_ports.map(gpio_port => new Servo(gpio_port));
var positions = [100,65,0,70];
const motors = [0,1,2,3].map(idx => new Servo(idx,positions[idx]));
initializePositions();


function initializePositions() {
    [0,1,2,3].map(idx => setPositions(idx, positions[idx],2000));
}

function setPositions(idx,value, interval) {
    var servo = motors[idx];
    //servo.goToAngle(value,interval);
    servo.setAngle(value);
    if(io != undefined)
        io.emit('positions', {idx, position: value});
}


var positionsMessage;

var io = StartServer(3000, function(socket) { 
    initializePositions();
    socket.on('positions', function(data) {
        console.log(">>> ", data);
        var idx = data.idx;
        var position = data.position;
        clearTimeout(positionsMessage);
        positionsMessage = setTimeout(() => {
            //console.log("Setting pulse to ", data);
        }, 100 );2
        setPositions(idx,position,data.interval);
    });
})
