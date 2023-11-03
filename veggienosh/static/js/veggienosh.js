$(document).ready(function() {
    // Initialize side navigation for mobile views
    $('.sidenav').sidenav();

    // Activate dropdown elements with MaterializeCSS
    $(".dropdown-trigger").dropdown();

    // Enhance 'select' elements with MaterializeCSS styling
    $('select').formSelect();

    // Ensure dropdowns have a valid selection before submitting
    // (Solution from StackOverflow: https://stackoverflow.com/questions/34248898/how-to-validate-select-option-for-a-materialize-dropdown)
    $("select[required]").css({
        display: "block",
        height: 0,
        padding: 0,
        width: 0,
        position: "absolute"
    });

    // Enable character counter for inputs with limited text length
    $('textarea#recipe_description, input#recipe_name').characterCounter();

    // Initialize tooltips for elements with additional information on hover
    $('.tooltipped').tooltip();

    // Attach modal functionality to modal-trigger elements
    $('.modal').modal();

    // Button visual feedback: Reset to original size when mouseout
    $("#btn-home").mouseout(function() {
        $(this).css("transform", "scale(1)");
    });

    // Button visual feedback: Enlarge slightly when mouseover
    $("#btn-home").mouseover(function() {
        $(this).css("transform", "scale(1.05)");
    });
});
