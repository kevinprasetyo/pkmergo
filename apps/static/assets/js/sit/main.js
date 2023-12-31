'use strict';

let timeThreshold = 300; // For 0.5 seconds;
let startAlgo = false;
let lastClosedTime,
	continuous = false;
let body = document.querySelector('body');
let message;

//entry point :
function main() {
	JEEFACETRANSFERAPI.init({
		canvasId: 'canvas',
		NNCpath: 'static/assets/js/sit/',
		callbackReady: function (errCode) {
			if (errCode) {
				console.log('ERROR - cannot init JEEFACETRANSFERAPI. errCode =', errCode);
				errorCallback(errCode);
				return;
			}
			console.log('INFO : JEEFACETRANSFERAPI is ready !!!');
			successCallback();
		} //end callbackReady()
	});
} //end main()

function successCallback() {
	// Call next frame
	nextFrame();
	document.getElementById('full-page-loader').style.display = 'none';
	body = document.querySelector('body');
	message = document.querySelector('#message');
	// Add code after API is ready.
}

function errorCallback(errorCode) {
	// Add code to handle the error
}

function nextFrame() {
	if (!startAlgo) {
		return;
	}
	let deltaTime = Date.now() - lastClosedTime;
	if (deltaTime > timeThreshold && continuous) {
		start_alarm();
		// console.log("Alarm Called");
		body.style.background = '#f00';
	} else {
		stop_alarm();
		body.style.background = '#fff';
	}

	if (JEEFACETRANSFERAPI.is_detected()) {
		// Do something awesome with rotation values
		let rotation = JEEFACETRANSFERAPI.get_rotationStabilized();
		let isHeadPostureOk = isHeadPostureOK(rotation);
		let positionScaleZ = JEEFACETRANSFERAPI.get_positionScale()[2];
		let screenDistanceOK = isScreenDistanceOK(positionScaleZ);

		if (!isHeadPostureOk[0] || !isHeadPostureOk[1] || !isHeadPostureOk[2] || !screenDistanceOK) {
			if (lastClosedTime === undefined || !continuous) lastClosedTime = Date.now(); // Now is the new time
			continuous = true;
			if (message) {
				let messageContent = '';
				if (!screenDistanceOK) {
					messageContent += '<h2>Terlalu dekat dengan layar</h2>';
				}
				if (!isHeadPostureOk[0]) {
					messageContent += '<h2>Kepala menekuk terlalu ke atas atau terlalu ke bawah</h2>';
				}
				if (!isHeadPostureOk[1]) {
					messageContent += '<h2>Kepala terlalu memuntir</h2>';
				}
				if (!isHeadPostureOk[2]) {
					messageContent += '<h2>Kepala menekuk ke arah bahu.</h2>';
				}
				message.innerHTML = messageContent;
			}
		} else {
			if (message) {
				message.innerHTML = '';
			}
			continuous = false;
		}

		//**************************************************************************** */

		// The API is detected
		console.log('Detected');
	} else {
		// Tell the user that detection is off.
		console.log('Not Detected');
	}
	// Replay frame
	requestAnimationFrame(nextFrame);
}

function start() {
	init_sound();
	startAlgo = true;
	nextFrame();
	document.getElementById('warnings').style.display = 'none';
}
