var deg = 0
setInterval(function(){
    deg++
    if(deg > 360) {
        deg = 0
    }
    document.body.style.background = 'linear-gradient(' + deg + 'deg, red, orange, yellow, green, blue, purple)'
}, 50)