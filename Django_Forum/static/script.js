////////////////////////////
// Javascript for Posts page
////////////////////////////

$(function() {
    // Executed when js-menu-icon is clicked
    $('.js-menu-icon').click(function() {
        // $(this) : self element, namely div.js-menu-icon
        // next() : Next to js-menu-icon, namely div.menu
        // toggle() : switch show and hide
        $(this).next().toggle();
    })
})