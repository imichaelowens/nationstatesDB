//Code inspiration from: https://stackoverflow.com/questions/34696208/play-a-sound-on-image-click-in-html

//Engine sound creative commons from: https://freesound.org/people/AdrianoAnjos/sounds/404299/
var engineAudio = new Audio('audio\\startup_ogg.ogg');
//Boiling sound creative commons from: https://freesound.org/people/Jace/sounds/19842/
var coolantAudio = new Audio('audio\\boiling_ogg.ogg');

  
var playingAudio = null;
function audioPlay(playingAudio) {
    if (engineAudio.play) {

    switch(playingAudio) {
        case 'engine':
            //pause other audio and set to zero
            coolantAudio.pause();
            coolantAudio.currentTime = 0;
            engineAudio.play();
            break;
        case 'coolant':
            //pause other audio and set to zero
            engineAudio.pause();
            engineAudio.currentTime = 0;
            coolantAudio.play();
            break;
    }
    }
    else {
        return;
    }
}


function carLights() {
element=document.getElementById('carLights');
if (element.src.match("images/licensed_light_off.jpg"))
  {
  element.src="images/licensed_light_on.jpg";
  }
else
  {
  element.src="images/licensed_light_off.jpg";
  }
}