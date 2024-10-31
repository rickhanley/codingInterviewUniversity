console.log("Hello");

const saveBtn = document.querySelector('.save-btn');
saveBtn.addEventListener('click', function(){
    console.log("You clicked save");
}) ;

document.querySelector(".myForm").addEventListener('submit', (event) =>{
    event.preventDefault();

    const data = new FormData(event.target);

    const firstName = data.get('firstName');
    const surName = data.get('surName');

    console.log(firstName);
    console.log(surName);

    console.log(data);
})
