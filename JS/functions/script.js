const formData = document.querySelector('.myForm').addEventListener('submit', event =>{
    event.preventDefault();

    const data = new FormData(event.target);
    const input = data.get('input');
    const container = document.querySelector(".container")

    for (i = 0; i < input.length; i++){
        console.log(input[i]);
        const div = document.createElement('div');
        div.classList.add("letters")
        div.innerHTML=`${input[i]}`;
        container.appendChild(div);
    }
    
})

let total = 0;
    for (i = 1; i < 101; i++){
        total += i;
    }
    console.log(total / 2);

    let n = 500000000;

    // Timing the loop method
    let startTimeLoop = performance.now();
    let sumLoop = 0;
    for (let i = 1; i <= n; i++) {
        sumLoop += i;
    }
    let endTimeLoop = performance.now();
    let timeTakenLoop = endTimeLoop - startTimeLoop; // Time in milliseconds
    
    // Timing the formula method
    let startTimeFormula = performance.now();
    let sumFormula = (n * (n + 1)) / 2;
    let endTimeFormula = performance.now();
    let timeTakenFormula = endTimeFormula - startTimeFormula; // Time in milliseconds
    
    // Output results
    console.log(`Sum using loop: ${sumLoop}`);
    console.log(`Time taken using loop: ${timeTakenLoop.toFixed(4)} milliseconds`);
    
    console.log(`Sum using formula: ${sumFormula}`);
    console.log(`Time taken using formula: ${timeTakenFormula.toFixed(4)} milliseconds`);