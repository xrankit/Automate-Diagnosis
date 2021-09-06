function imgSlider(anything){
    document.querySelector('.kits').src = anything;
}
function changeCircle(color){
    const circle = document.querySelector('.circle');
    circle.style.background = color;
}
function toggleMenu(){
    var menuToggle = document.querySelector('.toggle');
    var navigation = document.querySelector('.navigation');
    menuToggle.classList.toggle('active')
    navigation.classList.toggle('active')
}

var circle2 = document.getElementById("circle2")
var up = document.getElementById("up")
var down = document.getElementById("down")

var rotateValue = circle2.style.transform;
var rotateSum;

function rotate(){
    rotateSum = rotateValue + "rotate(-90deg)";
    circle2.style.transform = rotateSum;
    rotateValue = rotateSum;
}

function rotate1(){
    rotateSum = rotateValue + "rotate(90deg)";
    circle2.style.transform = rotateSum;
    rotateValue = rotateSum;
}


