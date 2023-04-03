function dragStart(event) {
    //datan asetus, tyyppi on teksti ja sisältö sen id:ssä oleva teksti
    event.dataTransfer.setData("Text",event.target.id)
}

function allowDrop(event) {
    event.preventDefault()

}

function drop(event) {
    event.preventDefault()
    const data = event.dataTransfer.getData("Text")
    event.target.appendChild(document.getElementById(data))
    var val = document.getElementById('translateWord')
    val.value=data
}