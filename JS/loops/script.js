const myArray = ["a", "b", "c"];
const myNumbers = [3,4,5,6,7,8,9];

myArray.forEach(element => {
    console.log(element.toUpperCase());

});

const mySentence = "this is all in upper case"

console.log(mySentence.toUpperCase());

for (let i = 0; i < 10; i++){
    console.log(i);
}

let counter = 0;
while (counter < 10) {
    console.log(counter);
    counter++;
};

function adder(a, b) {
    return a + b;
};

myNumbers.forEach(element => {
    console.log(adder(element, element));
});