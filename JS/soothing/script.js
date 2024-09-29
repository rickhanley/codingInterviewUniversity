console.log("hello");

const tiles_container = document.querySelector(".tiles-container");

const width = 16;
const height = 9;
const running = true;



function getRandomColour(){
    const colour_range = '25679C';
    let colour='#';
    for (let i = 0; i < 6; i++){
        colour += colour_range[Math.floor(Math.random() * 6)];
    };
    return colour;
};

for(let i = 0; i < width * height; i ++){
    const div = document.createElement('div');
    div.classList.add('tile');
    div.id = `${i}`;
    div.style.backgroundColor = getRandomColour();
    div.style.transition = 'background-color 0.4s ease';
    tiles_container.appendChild(div);
}

const tiles = document.querySelectorAll(".tile");

tiles.forEach(tile => {
    tile.addEventListener('mouseover', function(){
            tile.style.backgroundColor = getRandomColour();
            console.log(`Tile ${tile.id} tocuhed`)
        }
    );
});


function getRandomTile(){
    return Math.floor(Math.random()*143);
}

function getTime(seed){

    return Math.random() * seed;
    

}

function getTile(){
    return document.getElementById(getRandomTile())
}
// console.log(getTile());

// for (let i = 0; i < 300; i++){
//     console.log(getRandomTile());
// }
let wait_time = getTime();

let wait_time3 = getTime();
setInterval(function(){
    
    let tile = getTile();
    console.log("3");
    tile.style.backgroundColor = getRandomColour();
},wait_time3 = getTime(50));
