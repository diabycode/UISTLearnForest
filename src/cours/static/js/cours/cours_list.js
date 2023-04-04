
document.querySelectorAll(".course").forEach(course => {
    course.addEventListener("click", (e) => {
        e.target.closest(".course").querySelector(".course > a").click()
    })
})
