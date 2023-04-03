
var textval = []
var numval = []
var barColors = [];
var valueList = []
var labelList = ['right', 'wrong']
var labelSpeed = ['Download', 'upload']
var speeds = []

/*
function removeTextSrc()
{
   
        const element = document.getElementById('txtsrcBtnId')
        element.remove()
        window.location.reload()
    
}*/

//jos checkbox on valittu tämä funktio lisää sivulle uuden button elementin
function createTextSrc() {
    var word = document.getElementById('searchbox')
    if (document.getElementById('txtSrc').checked == true) {

      
        const addBtn = document.createElement('button')
        addBtn.setAttribute('class', 'txtsrcBtn')
        addBtn.innerHTML = 'Search'
        addBtn.setAttribute('id', 'txtsrcBtbId')

       
        document.body.append(addBtn)

        //määritellään onclick funktio painikkeelle tässä että se saadaan toimimaan vasta painikkeen klikkauksen
        //yhteydessä
        addBtn.onclick = function () {
            var word = document.getElementById('searchbox').value
            if (window.find(word)) {
                console.log(window.find(word))
            }


        }


    }
    else if (word==='clear') 
    {
        const addBtn = document.getElementById('txtsrcBtnId')
        addBtn.remove();
        

    }
}



function searchTxt(text) {
    console.log(text)
    if (window.find(text)) {
        console.log(window.find(text))
    }

}





//jos checkboxi on valittu luodaan uusi input elementti ja asetetaan setAttributella sille id-tunnus
function difAdd() {
    if (document.getElementById('dif').checked == true) {
        const addInput = document.createElement("input")
        addInput.setAttribute("id", "difAdd");
        document.body.append(addInput)
    }
}

function quiz() {
    if (document.getElementById('quest').checked == true) {
        document.getElementById('correctPlace').innerHTML = 'Correct'
    }
    else {
        document.getElementById('correctPlace').innerHTML = ''

    }
}

function netSpeed() {
    var download = document.getElementById('downSpeed').innerHTML;
    //käytetään replace metodissa regex-lauseketta jossa merkkijonosta poistetaan
    //kaikki ei-numerot paitsi piste. eli vain numerot ja piste jää muuttujaan
    download = download.replace(/[^\d.-]/g, '')

    speeds.push(download)
    var upload = document.getElementById('uploadSpeed').innerHTML;
    upload = upload.replace(/[^\d.-]/g, '')
    console.log(download)
    console.log(upload)
    speeds.push(upload)


    myChart = new Chart("myChart", {
        type: "bar",
        data: {
            labels: labelSpeed,
            datasets: [{
                backgroundColor: 'red',
                data: speeds
            }]
        },
        options: {
            legend: { display: false },
            title: {
                display: true,
                text: "Download & upload speeds"

            }
        }
    });
}
//kaavioiden piirto local storagesta haetuilla arvoilla
//alustetaan myChart funktion ulkopuolella, että sitä voidaan stats closestats funktioissa
var myChart = ''
function stats() {
    var correct = localStorage.getItem('clickcount')
    valueList.push(correct)

    var wrong = localStorage.getItem('wrongClick')
    valueList.push(wrong)

    console.log(correct)
    console.log(wrong)

    myChart = new Chart("myChart", {
        type: "bar",
        data: {
            labels: labelList,
            datasets: [{
                backgroundColor: 'red',
                data: valueList
            }]
        },
        options: {
            legend: { display: false },
            title: {
                display: true,
                text: "Your clicks"

            }
        }
    });
}

//tuhotaan pylväsdiagrammi
function closeStats() {

    myChart.destroy();
}
//localstoragen arvojen nollaus
function resetPoints() {
    localStorage.setItem('clickcount', 0)
    localStorage.setItem('wrongClick', 0)
    document.getElementById("clicksCount").innerHTML = 0
}



//funktio tekstin hakuun sivulta
var count = 0

//tekstinhaku sivulta, parametrina text = kenttään syötetty sana, background color= kovakoodattuna
//annettu taustaväri
function search(text, backgroundColor) {
    //jos parametrina saatua tekstiä ei löydetä eli se on false,näyetään haettu sana ja ilmoitus
    //sekä näytetään count muutujan arvo
    if (window.find(text) === false) {
        alert(text + ' not found')
        document.getElementById('total').innerHTML = 'Word was found ' + count + ' times';
    }

    else if (window.find && window.getSelection) {

        document.designMode = "on";
        //getselection on käyttäjän valitsema tekstialue / tai tekstin sijainti

        var sel = window.getSelection();
        sel.collapse(document.body, 0);


        while (window.find(text)) {
            document.execCommand("HiliteColor", false, backgroundColor);
            sel.collapseToEnd();
            count++

        }
        count = count - 1
        document.designMode = "off";

        document.getElementById('total').innerHTML = 'Word was found ' + count + ' times';

    }


}





//tällä funktiolla vaihdetaan iframe sourcea eli annetaan toistettavan videon sijainti
function ownLink() {


    //tallennetaan muuttujaan files oliotaulukon ensimäinen eli 0-kohta(tiedostonnimi)
    const selectedFile = document.getElementById("input").files[0];
    console.log(selectedFile)
    //tiedoston nimi yms tiedot tallennetaan olio taulukkoon haetaan ja tallennetaan muuttujaan
    //taulukon name ominaisuus eli tiedoston nimi
    var playfile = document.getElementById('url').value = selectedFile.name
    var playtime = document.getElementById("input").files[4];
    console.log(playtime)
    document.getElementById("filesize").value = playtime
    document.getElementById('iframe').src = '/static/upload/' + playfile


}

function video() {
    var srclink = document.getElementById('filepath').value;
    document.getElementById("source").setAttribute('src', '/static/upload/sample.mp4')

}


function barChart() {


    new Chart("myChart", {
        type: "bar",
        data: {
            labels: textval,
            datasets: [{
                backgroundColor: barColors,
                data: numval
            }]
        },
        options: {
            legend: { display: false },
            title: {
                display: true,
                text: "Barchart"

            }
        }
    });
}

function pieChart() {

    new Chart("myChart", {
        type: "pie",
        data: {
            labels: textval,
            datasets: [{
                backgroundColor: barColors,
                data: numval
            }]
        },
        options: {
            title: {
                display: true,
                text: "Piechart"
            }
        }
    });
}

//funktio lisää käyttäjän syöttämät arvot 2 eri listaan
function addList() {

    var col = document.getElementById("color").value
    var label = document.getElementById('textvalues').value;
    var numbers = document.getElementById('numvalues').value;

    textval.push(label)
    console.log(textval)
    numval.push(numbers)
    barColors.push(col)
    console.log(numval)
    document.getElementById('textvalues').value = "";
    document.getElementById('numvalues').value = "";
}

function download() {
    const imageLink = document.createElement('a')
    const canvas = document.getElementById('myChart')
    imageLink.download = 'canvas.png';
    imageLink.href = canvas.toDataURL('image/png', 1)
    console.log(imageLink.href)
    imageLink.click()
}





//JAVASCRITP FUNKTIO, JOLLA MUUTETAAN PSW1 & psw2 ID:N SISÄLTÄVÄ INPUT KENTÄN TYYPPI
//PASSWORDISTA TEKSTIKSI ELI NÄYTETÄÄN SIIHEN SYÖTETTY TEKSTI
//klikkausten alkuarvoksi annetaan yksi, että if/else lohko toimii halutulla tavalla.
//eli jos checkboxia klikataan näytetään salanana, kun klikkaus poistetaan ei näytetä
//salasanaa.
var clicks = 1;
function typeChanger() {
    clicks = clicks + 1
    if (clicks % 2 == 0) {
        document.getElementById("psw1").type = "text";
        document.getElementById("psw2").type = "text";
        document.getElementById("psw3").type = "text";
    }
    else {
        document.getElementById("psw1").type = "password";
        document.getElementById("psw2").type = "password";
        document.getElementById("psw3").type = "password";
    }
    //alert("The type of Input1 will now change from button to text");

}
//käyttäjätunnuksen tallennus local storageen
function rememberMe() {
    localStorage.setItem("user", document.getElementById("username").value);
    localStorage.setItem("password", document.getElementById("psw1").value);
}
//käyttäjätunnuksen haku localstoragesta
function getUser() {
    const userName = localStorage.getItem('user')
    const passWord = localStorage.getItem('password')
    if (userName === null && passWord == null) {
        alert('Local storage is empty!')
    }
    else {
        document.getElementById('username').value = userName;
        document.getElementById('psw1').value = passWord;

    }
}

function storage() {

    localStorage.setItem('Product', document.getElementById('products').value);


}

function cart() {
    var prod = document.getElementById('prod').value;

    alert('Product added to cart!')
}


function chartSave() {
    alert('chart is saved.')
}


// tuotteen määrän lisäys ja vähennystoiminnot toteuttavat funktiot
var clicks = 0;

function plus() {
    var checks = document.getElementById('cp').innerHTML;
    if (checks == 'OK') {
        clicks += 1;
        document.getElementById("clicks").innerHTML = clicks;

    }


}

function minus() {
    clicks = clicks - 1

}

function cancelDelete() {
    alert('Delete cancelled!')
}



//funktio joka pyytää käyttäjää vahvistamaan tilaustietojen poiston. jos käyttäjä
//vastaa myöntävästi eli confirm saa arvokseen truen, userinput kenttään lisätään sana
//delete. delete on if-lauseen ehtona seeorders.py tiedoston deleteOrder fuktiossa.
function ConfirmDel() {
    if (confirm('Are you sure you want to delete this?') == true) {
        document.getElementById("userInput").value = "delete";
    }
    else {
        document.getElementById("userInput").value = "cancel";
        //funktio jota kutsutaan jos userinput on cancel
        cancelDelete()
        return 0;

    }
}
//taulukkoon tallennetaan thisVal arvot eli käyttäjän syöttämät luvut.
//taulukkoa käytetään, että käyttäjä voi halutessaan syöttää useamman
//kuin yhden luvun input kenttään. ilman taulukkoa voi syöttää vain 
//yhden luvun syötekenttään
const numbers = []
const numbers2 = []
var check = ''
//lisätään eventlistnerit number1 ja 2 syötekenttiin, eli selvitetään
//kumpaa syötekenttää on klikattu (click) hiirellä
document.getElementById('number1'), addEventListener('click', clickCheck)
document.getElementById('number2'), addEventListener('click', clickCheck)

function clickCheck(event) {     //jos number1 syötekenttää on klikattu check apumuuttujan arvo on no, kutsutaa calculate funktiota
    if (event.target.id === "number1") {
        check = 'no';
        calculate()
    }
    //jos number2 kenttää on klikattu
    else if (event.target.id === 'number2') {
        check = 'yes';
        calculate()

    }

}
function calculate(thisVal) {//jos check muuttujan arvo on yes
    if (check === 'yes') {
        numbers2.push(thisVal)
        //join metodin avulla poistetaan pilkut numbers taulukkoon tallennettujen
        //numeroiden välistä.
        document.getElementById('number2').value = numbers2.join('')
        //number3 ja 4 on piilotettuja formin sisällä olevia kenttiä
        //joihin myös välitetään numerot koska formi ei näe sen ulkopuolella olevia.
        document.getElementById('number4').value = numbers2.join('')

    }
    else {
        numbers.push(thisVal)

        document.getElementById('number1').value = numbers.join('')
        document.getElementById('number3').value = numbers.join('')

    }
}












/*
function calculate(thisVal)
{
    const numbers = []
    numbers.push(thisVal)
    //jos number1 ja number2 kentät ovat tyhjiä
   if (number1.value.length==0 && number2.value.length==0)
   {    
    document.getElementById('number1').value = numbers

    //piilotettu calculate formin sisällä oleva input kenttä
    document.getElementById('number3').value = thisVal;
    
    

   }
   else
   {
    document.getElementById('number2').value = thisVal;

     //piilotettu calculate formin sisällä oleva input kenttä
    document.getElementById('number4').value = thisVal;
    

   }

}*/
function operator(thisVal) {
    document.getElementById('operator').value = thisVal
}


var empty = ""
function clear() {
    document.getElementById('number1').value = empty;


    //  document.getElementById('number2').value = "";
    // document.getElementById('operator').value = "";

}

