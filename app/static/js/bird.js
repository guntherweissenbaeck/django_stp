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
// Fundumstände
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


