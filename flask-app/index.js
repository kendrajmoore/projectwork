const getPods = async() => {
    let response = await fetch("http://127.0.0.1:5000/podcasts")
    let data = await response.json()
    let podz = data.podcasts

    let div = document.getElementById("podDiv");
    let rowContainer = document.createElement("div");
    rowContainer.className = "row-container";

    for(const pod of podz){
        let newDiv = document.createElement("div")
        let h1 = document.createElement("h1")
        h1.innerText = `${pod.title}`
        let h3 = document.createElement("h3")
        h3.innerText = `${pod.description}`
        let p1 = document.createElement("p")
        p1.innerText = `${pod.total_episodes}`
        let img = document.createElement("img")
        img.src = `${pod.thumbnail}`
        newDiv.appendChild(h1)
        newDiv.appendChild(h3)
        newDiv.appendChild(p1)
        newDiv.appendChild(img)
        rowContainer.appendChild(newDiv);

        if (rowContainer.children.length === 3) {
            div.appendChild(rowContainer);
            rowContainer = document.createElement("div");
            rowContainer.className = "row-container";
        }
    }
    if (rowContainer.children.length > 0) {
        div.appendChild(rowContainer);
    }
  
}


getPods()