async function fetchItem (itemId, itemType) {
    const response = await fetch(`/cours/items/${itemId}/${itemType}/`, {
        method: "GET",
        headers: {
            "Accept": "application/json",
        }
    })

    if (response.ok) {
        return await response.json()
    }

}



const items = document.querySelectorAll(".section > li")

// add listening 
items.forEach(element => {
    element.addEventListener("click", e => {
        fetchItem(e.target.dataset.id, e.target.dataset.type)
            .then(item => {
                console.log(item)
                if (item.object.type === "video") {
                    document.querySelector(".my-player").innerHTML = item.object.source
                } else {
                    // article
                    document.querySelector(".right").innerHTML = item.object.content

                }
            })

    })
});




