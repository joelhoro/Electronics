// @ts-check
"use strict";
debugger; 
var ads1x15 = require('node-ads1x15');  



class JoyStick {

    constructor() {
        this.samplingFrequency = 1000;
        this.position = {}
        this.initialize();
    }

    async initialize() {

                
        var chip = 0; //0 for ads1015, 1 for ads1115  
        
        //Simple usage (default ADS address on pi 2b or 3):
        var adc = new ads1x15(chip); 
        
        // Optionally i2c address as (chip, address) or (chip, address, i2c_dev)
        // So to use  /dev/i2c-0 use the line below instead...:
        var idx = 0;        
        //    var adc = new ads1x15(chip, 0x48, 'dev/i2c-0');
        setInterval(() => {

            var channel = 0; //channel 0, 1, 2, or 3...  
            var samplesPerSecond = '250'; // see index.js for allowed values for your chip  
            var progGainAmp = '4096'; // see index.js for allowed values for your chip  
            
            if(!adc.busy)  
            {  
                adc.readADCSingleEnded(0, progGainAmp, samplesPerSecond, (err,data) => {
                    console.log(0,data);
                    this.position.x = data
                    adc.readADCSingleEnded(1, progGainAmp, samplesPerSecond, (err,data2) => {
                        console.log(0,data2);
                    this.position.y = data2;
                        console.log(idx++, this.position);
                    });
                });
            }
        }, 1000);//this.samplingFrequency);
    }
}
    
var joyStick = new JoyStick();
