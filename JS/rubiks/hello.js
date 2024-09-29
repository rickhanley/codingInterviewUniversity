console.log("Hi");

const tiles = document.getElementsByClassName("tile");
const colour_array = ["red", "white", "green", "blue", "orange", "yellow"];

function colour_picker(){

    let index = 0;
    console.log(colour_array)
    index = colour_array[Math.floor(Math.random() * 6)];
    console.log(index)
    return index 
}

colour_picker()

for (let tile of tiles){
    tile.classList.add(colour_picker());
}



console.log(tiles);