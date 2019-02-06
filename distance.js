const DistanceSensor = require('./distanceSensor').DistanceSensor;

var distanceSensor = new DistanceSensor(23,24);

const StartServer = require('./server').StartServer;

var io = StartServer(3000);

distanceSensor.start(250,distance => io.emit('distance', distance));
