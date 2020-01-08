var deg = 0 //Degree to rotate background
setInterval(function(){ //Run the code on an interval
    deg++   //Increment degree
    if(deg > 360) { //If deg is more than 360
        deg = 0 //Reset to 0 just for convenience
    }
    document.body.style.background = 'linear-gradient(' + deg + 'deg, red, orange, yellow, green, blue, purple)'    //Set the background to the rotation and the rainbow
}, 50)  //Execute function at 50ms

var links = document.getElementsByTagName('a')  //Get all links (<a>) in the document
for(var i = 0; i < links.length; i++) { //Iterate through links
    links[i].addEventListener('click', function(e) {    //Add a click event listener to that link
        e.preventDefault()  //Prevent default browser action for when the user clicks the link
        console.log('Workaround initiate')
        window.open(e.target.href)  //Instead open a new window at that link (workaround?)
    })
}



/*
SIDE NOTE:
Eventually implement a WebSocket server from the main Python script, and connect using JavaScript to communicate events and transmit data. Alternatively implement an HTTP server and use GET/POST. wxPython doesn't seem to have event listeners between JavaScript and Python. If it does, I'm too lazy to learn the code for it. I will just take the more complex route and make a WebSocket server and communicate that way.
*/