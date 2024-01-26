// --------------------------------------------
// Statusänderung
// --------------------------------------------

function changeDateOnStatusChange() {
    // change id_status_changed_at to current date
    let statusChangedAtField = document.getElementById("id_status_changed");
    let statusChangedAt = new Date().toISOString().slice(0, 10);
    statusChangedAtField.value = statusChangedAt;
}

// Load function on change.
document.getElementById("id_status").addEventListener("change", (event) => {
    (changeDateOnStatusChange)();
});