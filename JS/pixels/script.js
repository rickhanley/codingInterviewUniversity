import bob from './millie.js';

// console.log(bob);

const pixel_container = document.querySelector(".pixel-container");

let width = 128;
let height = 85;
const rgbTriple = 3;
const rowWidth = width * rgbTriple;

const imageSize = width * height * rgbTriple;
console.log(imageSize);

for(let i = 0; i < height; i = i + 1){
    for (let j = imageSize - (rowWidth * (i + 1)); j < imageSize - (rowWidth * i); j = j + 3)
    {
        console.log(i);
        let red = parseInt(bob[j], 10);
        let green = parseInt(bob[j + 1], 10);
        let blue = parseInt(bob[j + 2], 10);
        let colour = `#${red.toString(16).padStart(2, '0')}${green.toString(16).padStart(2, '0')}${blue.toString(16).padStart(2, '0')}`

        const div = document.createElement('div');
        div.classList.add('pixel');
        div.style.backgroundColor = colour;
        div.id = `${i / 3}`;
        console.log(div.id)
        pixel_container.appendChild(div); 
    };
};