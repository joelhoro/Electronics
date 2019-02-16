// var oled = require('oled-js-pi');
 
// var opts = {
//   width: 128,
//   height: 64,
//   address: 0x3C
// };
 
// var oled = new oled(opts);
// oled.drawPixel([
//   [128, 1, 1],
//   [128, 32, 1],
//   [128, 16, 1],
//   [64, 16, 1]
// ]);

function go(){
  // write some text
  g.drawString("Hello World!",2,2);
  // write to the screen
  g.flip(); 
 }
 // I2C
 I2C1.setup({scl:B6,sda:B7});
 
 var g = require("SSD1306").connect(I2C1, go);
 // or
 var g = require("SSD1306").connect(I2C1, go, { address: 0x3C });
 
 // SPI
 var s = new SPI();
 s.setup({mosi: B6, sck:B5});
 var g = require("SSD1306").connectSPI(s, A8, B7, go);
 