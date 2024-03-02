// --------------------------------------------
// Fundort
// --------------------------------------------

function showHidePlaceFoundOther() {
    let placeFoundField = document.getElementById("id_place_found");
    let placeFoundText = placeFoundField.options[placeFoundField.selectedIndex].text;
    let placeFoundOtherField = document.getElementById("div_id_place_found_other");

    if (placeFoundText == 'anderer Ort') {
        placeFoundOtherField.hidden = false
    } else {
        placeFoundOtherField.hidden = true
    }
}


// Load function on windows load.
(showHidePlaceFoundOther)();


// Load function on change.
document.getElementById("id_place_found").addEventListener("change", (event) => {
    showHidePlaceFoundOther()
});

// --------------------------------------------
// Fundumstaende
// --------------------------------------------

function showHideCircumstancesOther() {
    let circumstancesField = document.getElementById("id_find_circumstances");
    let circumstancesText = circumstancesField.options[circumstancesField.selectedIndex].text;
    let circumstancesOtherField = document.getElementById("div_id_find_circumstances_other");

    if (circumstancesText == 'andere Fundumstände') {
        circumstancesOtherField.hidden = false
    } else {
        circumstancesOtherField.hidden = true
    }
}


// Load function on windows load.
(showHideCircumstancesOther)();


// Load function on change.
document.getElementById("id_find_circumstances").addEventListener("change", (event) => {
    showHideCircumstancesOther()
});


// --------------------------------------------
// Status Vermittlung
// --------------------------------------------

function showHideStatusMediation() {
    let statusField = document.getElementById("id_status");
    let statusText = statusField.options[statusField.selectedIndex].text;
    let statusMediationField = document.getElementById("div_id_status_mediation");

    if (statusText == 'Vermittlung') {
        statusMediationField.hidden = false
    } else {
        statusMediationField.hidden = true
    }
}


// Load function on windows load.
(showHideStatusMediation)();


// Load function on change.
document.getElementById("id_status").addEventListener("change", (event) => {
    showHideStatusMediation()
});


