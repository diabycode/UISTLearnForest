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


// add select item listening 
const items = document.querySelectorAll(".section > li")
items.forEach(element => {
    element.addEventListener("click", e => {
        fetchItem(e.target.dataset.id, e.target.dataset.type)
            .then(item => {
                if (item.object.type === "video") {
                    // get video player template
                    const videoTemplate = document.querySelector("#video-player-template").content.cloneNode(true)
                    videoTemplate.querySelector(".my-player").innerHTML = item.object.source
                    videoTemplate.querySelector(".infos h3").innerText = item.object.title
                    videoTemplate.querySelector(".infos p").innerText = item.object.description
                    
                    // add video player to the right
                    document.querySelector(".right .content").innerHTML = ""
                    document.querySelector(".right .content").appendChild(videoTemplate)
                    window.scrollTo(0, 0)
                    
                } else {
                    // get article template
                    const articleTemplate = document.querySelector("#article-template").content.cloneNode(true)
                    articleTemplate.querySelector("h3").innerText = item.object.title
                    articleTemplate.querySelector("div").innerText = item.object.content

                    // add article to the right
                    document.querySelector(".right .content").innerHTML = ""
                    document.querySelector(".right .content").appendChild(articleTemplate)
                    window.scrollTo(0, 0)

                }
            })

    })
});


// select default item
document.querySelector(".cours-sections .item").click()