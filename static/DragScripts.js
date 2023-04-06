




//muutetaan input-kentän taustaväriä, kun kenttää on klikattua
function changeColor()
{
const inputField = document.getElementById("translateWord");
//värin vaihto kun kenttä on aktiivisena eli = focusin
inputField.addEventListener("focusin", (event) => {
  event.target.style.background = "yellow";
});
//kun kenttä ei ole aktiivinen eli = focusout
inputField.addEventListener("focusout", (event) => {
  event.target.style.background = "";
});

}




function dragStart(dragevent) {
    //datan asetus, tyyppi on teksti ja sisältö sen id:ssä oleva teksti
    dragevent.dataTransfer.setData("text/plain",dragevent.target.id)
}

function allowDrop(event) {
    event.preventDefault()

}

function drop(dropevent) {
    dropevent.preventDefault()
    const data = dropevent.dataTransfer.getData("text")
    dropevent.target.appendChild(document.getElementById(data))
    var val = document.getElementById('translateWord')
    val.value=data
}