$(document).ready(function() {
    // Smooth scrolling for anchor links
    $('a[href*="#"]').on('click', function(e) {
        e.preventDefault();
        $('html, body').animate({
            scrollTop: $($(this).attr('href')).offset().top
        }, 500, 'linear');
    });

    // Toggle navbar collapse on click
    $('.navbar-nav>li>a').on('click', function(){
        $('.navbar-collapse').collapse('hide');
    });


    // Initialize tooltips
    $('[data-toggle="tooltip"]').tooltip();

    // Initialize popovers
    $('[data-toggle="popover"]').popover();

    // WhatsApp Floating Icon
    $('.whatsapp-float').on('click', function() {
        var phone = '256779366796'; // Replace with your WhatsApp number
        var message = encodeURIComponent('Hello from Bright Future Products!');
        var whatsappUrl = 'https://wa.me/' + phone + '?text=' + message;
        window.open(whatsappUrl, '_blank');
    });

    // Other custom scripts specific to your project
    // Add here as needed

});