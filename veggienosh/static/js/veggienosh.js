$(document).ready(function() {
    // Initialize side navigation for mobile views
    $('.sidenav').sidenav();

    // Activate dropdown elements with MaterializeCSS
    $(".dropdown-trigger").dropdown();

    // Enhance 'select' elements with MaterializeCSS styling
    $('select').formSelect();

    // Ensure dropdowns have a valid selection before submitting
    // Solution from StackOverflow to ensure 'select' elements are validated: 
    // https://stackoverflow.com/questions/34248898/how-to-validate-select-option-for-a-materialize-dropdown
    $("select[required]").css({
        display: "block",     
        height: 0,           
        padding: 0,           
        width: 0,             
        position: "absolute"  
    });

    // Enable character counter for inputs with limited text length
    // Attaches a character counter to text areas and inputs for user feedback on length
    $('textarea#recipe_description, input#recipe_name').characterCounter();

    // Initialize tooltips for elements with additional information on hover
    // Tooltips provide additional context or information to the user when they hover over an element
    $('.tooltipped').tooltip();

    // Attach modal functionality to modal-trigger elements
    // This initializes all elements with the 'modal' class to function as modals (pop-up elements)
    $('.modal').modal();

    // Button visual feedback: Reset to original size when mouseout
    // When the user's cursor leaves the button, reset its scale to 1 (normal size)
    $("#btn-home").mouseout(function() {
        $(this).css("transform", "scale(1)");
    });

    // Button visual feedback: Enlarge slightly when mouseover
    // When the user's cursor hovers over the button, increase its scale to 1.05 (slightly larger)
    $("#btn-home").mouseover(function() {
        $(this).css("transform", "scale(1.05)");
    });
});

// Initialize social media share dropdowns after full page load.
// This ensures all elements for sharing recipes are interactive and data-rich.
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.dropdown-trigger'); 
    var instances = M.Dropdown.init(elems, {}); 
});

// Search bar functionality
// Clears the content of the input field when the clear button is clicked.
function clearSearch() {
    document.getElementById('query').value = '';
}
