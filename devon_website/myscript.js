let progress = document.getElementById('progressbar');
let totalHeight = document.body.scrollHeight - window.innerHeight;

let panels = [];
let currentPanel = 0;
let panelElements = document.getElementsByClassName('panel');

// Puts all panel IDs into an array
for (let i = 0; i < panelElements.length; i++) {
    panels.push(panelElements[i].id);
}

// Sets window back to top on refresh and reset currentPanel
function setVars() {
    window.scrollTo(0, 0);
    currentPanel = 0;
}

function scrollToTop() {
    window.scrollTo(0, 0);
    currentPanel = 0;
}

// Calculates how far down the screen is compared to screen height
function scrollProgress() {
    let progressHeight = (window.scrollY / totalHeight) * 100;
    progress.style.height = progressHeight + '%';
}

// Funny sleep function
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// Insane awesome typewriter function that appends to element with id 'name'
async function typewrite() {
    var h = document.getElementById('name');
    const sentences = ["Devon Garls", "Programmer", "Swimmer", "Music-er", "Devon Garls"];

    for (let i = 0; i < sentences.length; i++) {

        let sentence = sentences[i];

        for (let j = 0; j < sentence.length; j++) {
            if (sentence.charAt(j) != " ") {
                await sleep(300);
            }
            h.innerHTML += sentence.charAt(j);
        }

        h.style.animation = "blinking_cursor 0.5s step-end infinite"
        if (i === sentences.length - 1) {
            h.style.animation = "blinking_cursor 1s step-end infinite"
            break;
        }
        await sleep(1000);
        h.style.animation = "none"

        for (let j = 0; j < sentence.length; j++) {
            if (h.innerHTML.charAt(j) != " ") {
                await sleep(100);
            }
            h.innerHTML = h.innerHTML.substring(0, h.innerHTML.length - 1);
        }
    }
}

// Brings the topbar down
function bringbar() {
    const topbar = document.getElementById("topbar");
    if (currentPanel != 0) {
        topbar.style.top = "0";
    }
    else {
        topbar.style.top = "-5%";
    }
}

// Brings the movement arrow down
function bringArrowDown(element) {
    if (currentPanel === 0 && element.id == 'uparrow') return;
    element.style.transform = "scale(1.2) translateY(10vh)";
}

// Brings the movement arrow up
function bringArrowUp(element) {
    if (currentPanel === 3 && element.id == 'downarrow') return;
    element.style.transform = "scale(1.2) translateY(-10vh)";
}

//Scrolls to the next panel down
function moveScreenDown() {
    currentPanel += 1;
    if (currentPanel >= 3) {
        currentPanel = 3;
        bringArrowDown(document.getElementById('downarrow'));
    }
    window.scrollTo(0, document.getElementById(panels[currentPanel]).offsetTop);
}

//Scrolls to the next panel above
function moveScreenUp() {
    currentPanel -= 1;
    if (currentPanel <= 0) {
        currentPanel = 0;
        bringArrowUp(document.getElementById('uparrow'));
    }
    window.scrollTo(0, document.getElementById(panels[currentPanel]).offsetTop);
}


window.onload = function () {
    typewrite();
    //setVars()
};
window.onscroll = function () {
    bringbar();
    scrollProgress();
};
