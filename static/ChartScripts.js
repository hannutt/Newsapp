var textval = []
var numval = []
var barColors = [];
var valueList = []
var labelList = ['right', 'wrong']
var labelSpeed = ['Download', 'upload']

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

function closeStats() {

    myChart.destroy();
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
