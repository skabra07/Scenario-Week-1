// Get the modal
var add = document.getElementById('addModal');


// Get the button that opens the modal
var addbtn = document.getElementById("add");


// Get the <span> element that closes the modal
var closeElement = document.getElementsByClassName("close");
addspan = closeElement[closeElement.length - 1];

// When the user clicks the button, open the modal 
addbtn.onclick = function() {
    add.style.display = "block";
}


// When the user clicks on <span> (x), close the modal
addspan.onclick = function() {
    add.style.display = "none";
}


// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == add) {
        add.style.display = "none";
    }
}