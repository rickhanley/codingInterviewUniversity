const container = document.createElement('div');
container.classList.add('container'); 
document.body.appendChild(container); 



const para = document.createElement('p')
para.classList.add('para')
container.appendChild(para)

para.innerHTML = "Hello World";

const items = ["one", "two", "three"];

items.forEach(item => {
    const div = document.createElement('div');
    div.classList.add('contentbox');
    container.appendChild(div);
})