my_list = ["Email so and so", "Send contract", "Download CSV", "Prepare report", "Attend meeting", "Get data from mainframe", "Repair fax machine", "Order paper", "Arrange annual conference", "Arrange meeting with funder", "Year end procedures"]
// my_list = ["Email so and so", "Send contract", "Download CSV", "Prepare report", "Attend meeting", "Get data from mainframe", "Repair fax machine"]

const modal = document.querySelector(".myModal");
const modalContent = document.querySelector(".modal-content")

function modalToggle() {
    if(modal.style.display == "block") {
    modal.style.display = "none";
    } else {
       modal.style.display = "block";
    }
}

function makeDivs() {
    // get the container you want to use
    const scrollable = document.querySelector(".scrollable");
    // forEach to run over the list and create elements
    my_list.forEach((list_name) => {
        // create a div constant and create a div element i.e. the tag
        const div = document.createElement('div');
        // insert the classname to the tag
        div.className = 'item';
        // insert the text content i.e. the content from the list
        div.textContent = list_name;
        // add an event listener to each new div created. 
        // listens for a click, returns the "list_name"
        // i.e. the content for that list item in the console 
        // to confirm working
        div.addEventListener('click', () => {
            console.log(`You clicked on ${list_name}`);
            modalToggle();
        });
        // append the newly created divs to the variable represeneting the container
        scrollable.appendChild(div);
    });
}    
document.addEventListener('DOMContentLoaded', makeDivs);

document.querySelector(".close-btn").addEventListener('click', modalToggle);