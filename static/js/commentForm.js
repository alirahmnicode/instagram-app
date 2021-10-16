var btn = document.getElementsByClassName("show-comment-form");
var i;

for (i = 0; i < btn.length; i++) {
    btn[i].addEventListener("click", function () {
        var form = this.nextElementSibling;
        form.classList.toggle("active");
        if (form.style.overflow === "visible") {
            form.style.height = '0px'
            form.style.overflow = "hidden";
        } else {
            form.style.height = '30px'
            form.style.overflow = "visible";
        }
    });
}
