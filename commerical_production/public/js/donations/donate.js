// this identifies your website in the createToken call below
Stripe.setPublishableKey(stripe_public_key);

function stripeResponseHandler(res) {
    if (res.error) {
        // show the errors on the form
        $(".payment-errors").text(res.error.message).removeClass('hidden');
    } else {
        var $form = $("#payment-form");
        // token contains id, last4, and card type
        var token = res.id;
        // insert the token into the form so it gets submitted to the server
        $form.append("<input type='hidden' name='stripeToken' value='" + token + "'/>");
        // and submit
        $form.get(0).submit();
    }
}

function submitPaymentForm(e){
    $('.payment-errors').addClass('hidden');
      var token = stripeResponseHandler;
      var amount = parseInt($("#id_amount").val());
      var description = $("#id_reason").val();
      if (!isNaN(amount)) {
        description += " ($" + amount + ".00)"
        amount = amount*100;//in cents
      } else {
        amount = null
      }
      StripeCheckout.open({
        key:         stripe_public_key,
        amount:      amount, 
        name:        "Burton Third Online",
        description:  description,
        image:       "/public/img/btb-logo.png",
        panelLabel:  "Checkout",
        token:       token,
      });

      return false;
    }

$(document).ready(function() {
    $('#customButton').click(submitPaymentForm);
});