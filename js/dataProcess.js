//Created by Michael Owens

var intDoors = null;
var intMiles = null;
var strBudget = null;
var strInterst = null;

const form = document.querySelector("#carsForm");
let userAnswers = [];

form.onsubmit = getData;

function getData() {
    //var assignments
        //Doors
        intDoors = document.getElementById('doors').value;
        //Miles
        intMiles =  document.getElementById('milesDriven').value;
        

    //vars to get checked status
    var interestRadios = document.getElementsByName('qInterest');
    var budgetRadios = document.getElementsByName('qBudget');

//Interested Cars Pick List

for (var i = 0, length = interestRadios.length; i < length; i++) {
  if (interestRadios[i].checked) {
    userAnswers.push(interestRadios[i].value);
    break;
  }
}

//Budget Pick List

for (var i = 0, length = budgetRadios.length; i < length; i++) {
    if (budgetRadios[i].checked) {
      userAnswers.push(budgetRadios[i].value);
      break;
    }
  }

//Process the data
processData();
// Do Not Reload The Webpage
return false;
}




function processData() {
    
    //assign vars from array
    strInterst = userAnswers[0];
    strBudget = userAnswers[1];

    
    //Begin decision structure
    var gasCalculated = intMiles;
    var prefChart = null;
    var priceChart = null;
    var nextPage = null;
    var gasNotification = document.getElementById("gasNotification");
    var carsFormVisable = document.getElementById("carsForm");
    var qIntroVisable = document.getElementById("qIntro");
    

    if (strBudget == 'A') {
        prefChart = document.getElementById("economyPref");
        priceChart = document.getElementById("economyPrice");
        nextPage = document.getElementById("learnMore");
        prefChart.classList.toggle("d-none");
        priceChart.classList.toggle("d-none");
        nextPage.classList.toggle("d-none");
        carsFormVisable.classList.toggle("d-none");
        qIntroVisable.classList.toggle("d-none");
        

        prefChart = null;
        priceChart = null;
    }else if (strBudget == 'B') {
        prefChart = document.getElementById("midsizePref");
        priceChart = document.getElementById("midsizePrice");
        nextPage = document.getElementById("learnMore");
        prefChart.classList.toggle("d-none");
        priceChart.classList.toggle("d-none");
        nextPage.classList.toggle("d-none");
        carsFormVisable.classList.toggle("d-none");
        qIntroVisable.classList.toggle("d-none");
        



        prefChart = null;
        priceChart = null;
    }else if (strBudget == 'C') {
        prefChart = document.getElementById("fullsizePref");
        priceChart = document.getElementById("fullsizePrice");
        nextPage = document.getElementById("learnMore");
        prefChart.classList.toggle("d-none");
        priceChart.classList.toggle("d-none");
        nextPage.classList.toggle("d-none");
        carsFormVisable.classList.toggle("d-none");
        qIntroVisable.classList.toggle("d-none");
        


        prefChart = null;
        priceChart = null;
    }else if (strBudget == 'D') {
        prefChart = document.getElementById("sportsPref");
        priceChart = document.getElementById("sportsPrice");
        nextPage = document.getElementById("learnMore");
        prefChart.classList.toggle("d-none");
        priceChart.classList.toggle("d-none");
        nextPage.classList.toggle("d-none");
        carsFormVisable.classList.toggle("d-none");
        qIntroVisable.classList.toggle("d-none");
       


        prefChart = null;
        priceChart = null;
    }

    gasCalculated = gasCalculated/30; //Average MPG for a 2020 car
    gasCalculated = gasCalculated * 2.2; //miles multiplied by average national price/gal
    gasCalculated = gasCalculated + 160.00 //Gas plus average yearly oil maintence
    gasCalculated = gasCalculated.toFixed(2);

    gasNotification.classList.toggle("d-none");
    gasNotification.textContent = "Based on the amount of driving you will do this year we calculate you will spend around $" + gasCalculated + " for gas and oil changes.";



return false;
}
