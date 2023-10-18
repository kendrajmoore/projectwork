const nodeList = document.getElementsByTagName("LI");
nodeList.forEach(node => {
    const span = document.createElement("SPAN");
    const txt = document.createTextNode("\u00D7");
    span.className = "close";
    span.appendChild(txt);
    node.appendChild(span);
});


const closeButtons = document.querySelectorAll(".close");
closeButtons.forEach(button => {
    button.addEventListener('click', () =>{
        const div = button.parentElement;
        div.style.display = "none";
    });
});

const list = document.querySelector('ul');
list.addEventListener('click', ev => {
    if(ev.target.tagName === 'LI'){
        ev.target.classList.toggle('checked');
    }
});

function newElement() {
    const li = document.createElement("li");
    const inputValue = document.getElementById("myInput").value;
    const t = document.createTextNode(inputValue);
    li.appendChild(t);
    
    if (inputValue === '') {
        alert("You must write something!");
    } else {
        document.getElementById("myUL").appendChild(li);
    }
    document.getElementById("myInput").value = "";

    const span = document.createElement("SPAN");
    const txt = document.createTextNode("\u00D7");
    span.className = "close";
    span.appendChild(txt);
    li.appendChild(span);

    span.addEventListener('click', () => {
        const div = span.parentElement;
        div.style.display = "none";
    });
}




