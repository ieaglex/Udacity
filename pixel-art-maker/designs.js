// Select color input
var color = document.getElementById('colorPicker');
// Select size input
sizePicker.addEventListener('submit', function (submit) {
    submit.preventDefault();
    var gridHeight = document.getElementById('inputHeight').value;
    var gridWidth = document.getElementById('inputWidth').value;
    makeGrid(gridHeight, gridWidth)
});

// When size is submitted by the user, call makeGrid()
function makeGrid(gridHeight, gridWidth) {
    var designCanvas = document.getElementById('pixelCanvas');
    pixelCanvas.innerHTML = '';
    for (let a = 0; a < gridHeight; a++) {
        let row = designCanvas.insertRow(-1);
        for (let b = 0; b < gridWidth; b++) {
            let cell = row.insertCell(0);
            cell.addEventListener('click', function() {
                cell.style.backgroundColor = color.value;
            });
        }
    }
}
