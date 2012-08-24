// this identifies your website in the createToken call below
Stripe.setPublishableKey(stripe_public_key);

function stripeResponseHandler(status, response) {
    if (response.error) {
        // show the errors on the form
        $(".payment-errors").text(response.error.message);
        $(".submit-button").removeAttr("disabled");
    } else {
        var form$ = $("#payment-form");
        // token contains id, last4, and card type
        var token = response['id'];
        // insert the token into the form so it gets submitted to the server
        form$.append("<input type='hidden' name='stripeToken' value='" + token + "'/>");
        // and submit
        form$.get(0).submit();
    }
}

function submitPaymentForm(e) {
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
}

function addTips() {
    makeTip('submit_button', "Your card information never touches our servers and is handled entirely by the Stripe API. Fear not :)", 'right', 'hover');
}

$(document).ready(function() {
    addTips(); // on submit button
    $("#payment-form").submit(submitPaymentForm);
});