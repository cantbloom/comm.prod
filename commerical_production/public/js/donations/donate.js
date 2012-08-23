// this identifies your website in the createToken call below
Stripe.setPublishableKey('pk_BTqYVmxjL4J3IJ0pBF8rMISKJpqU0');

function stripeResponseHandler(status, response) {
    if (response.error) {
        // re-enable the submit button
        $('.submit-button').removeAttr("disabled").removeClass("disabled");
        // show the errors on the form
        $(".payment-errors").removeClass("hidden").html(response.error.message);
    } else {
        var form$ = $("#payment-form");
        // token contains id, last4, and card type
        var token = response['id'];
        // insert the token into the form so it gets submitted to the server
        form$.append("<input type='hidden' name='stripeToken' value='" + token + "' />");
        // and submit
        form$.get(0).submit();
    }
}

function addTips() {
    makeTip('id_save_card', "Your card information never touches our servers and is handled entirely by the Stripe API.", 'right', 'hover');
}

function displayPaymentOptions() {
    if (saved_card_info) {
        $('.stripe-form').removeClass('hidden');
    } else {
        $('.saved-info').removeClass('hidden');
    }
}

$(document).ready(function() {
    addTips();
    displayPaymentOptions();
    $("#payment-form").submit(function(event) {
        // disable the submit button to prevent repeated clicks
        $('.submit-button').attr("disabled", "disabled");
        // createToken returns immediately - the supplied callback submits the form if there are no errors
        Stripe.createToken({
            number: $('.card-number').val(),
            cvc: $('.card-cvc').val(),
            exp_month: $('.card-expiry-month').val(),
            exp_year: $('.card-expiry-year').val()
        }, stripeResponseHandler);
        return false; // submit from callback
    });
});