var mqtt = require('mqtt');
var dateFormat = require('dateformat');
var client  = mqtt.connect({ host: 'localhost', port: 1883 })
client.on('connect', async function () {  
	for(i=0; i<200; i++){
		sendingdata("py787b-vx40");
		await sleep(5000);
		// sendingdata("py787b-mw47");
		// await sleep(1500);
		// sendingdata("py787b-qo06");
		// await sleep(1500);
	}

});
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function getRandomArbitrary(min, max) {
  return Math.random() * (max - min) + min;
}

function sendingdata(device_code){
	send = {
		device_code:device_code,
		date_add:dateFormat(new Date(), "yyyy-mm-dd HH:MM:ss"),
		gps:{
			latitude:-7.275973 + ( getRandomArbitrary(1,100) / 1000 ),
			longitude:112.808304 - ( getRandomArbitrary(1,100) / 1000 )
		},
		temperature: Math.floor(getRandomArbitrary(2000,3500)) / 100,
		fuel:800,
	}
	client.publish('message/sensor/py787b',JSON.stringify(send));
  	console.log(send);
}

