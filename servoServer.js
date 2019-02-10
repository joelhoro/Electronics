var StartServer = require('./server').StartServer;
var Servo = require('./servo2').Servo;

// connect yellow wire with pin 4 (#7)
// red to 5V / black to ground
//const gpio_ports = [4,18,23,24];
//const motors = gpio_ports.map(gpio_port => new Servo(gpio_port));

var config = [
    {
        name: 'Upper arm',
        channel: 0,
        position: 100,
    },
    {
        name: 'Body',
        channel: 1,
        position: 65,
    },
    {
        name: 'Gripper',
        channel: 2,
        position: 0,
    },
    {
        name: 'Lower arm',
        channel: 3,
        position: 70,
    },
]

var positions = config.map(record => record.position);
const motors = config.map(record => new Servo(record.channel,record.position));
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
    socket.emit('config', config);
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
