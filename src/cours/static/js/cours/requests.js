// // create HTML element with attributes given in object
// function createElement (tag, attributes) {
//     const element = document.createElement(tag)
//     for (const key in attributes) {
//         element.setAttribute(key, attributes[key])
//     }
//     return element
// }


// // get all cours objects
// export async function getCours () {
//     const r = await fetch('/cours/get/', {
//         method: 'GET',
//         headers: {
//             Accept: 'application/json',
//         }
//     })

//     if (r.status == 200) {
//         return await r.json()
//     }
// }

// getCours()
//     .then(cours => {
//         const coursTemplate = document.querySelector('#cours-template').content.cloneNode(true)

//         for (const c of cours.cours) {
            
//             coursTemplate.querySelector("h3").innerText = c.title
//             coursTemplate.querySelector("p").innerText = c.description

//             let e = createElement('div', {class: 'cours'})
//             e.appendChild(coursTemplate)

//             // add cours to the DOM
//             document.querySelector('#all-cours').prepend(e)
//         }
        
//     })

