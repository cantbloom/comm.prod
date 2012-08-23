function addEmail (e, d) {
    e.preventDefault();
    $('#add-email').before('<p class="alt-email"><input type="email" class="fancy-input" placeholder="Alternative Email" name="alt_email" data-original-title=""><a class="btn remove-email"><i class="icon-minus"></i></a></p>')
}

function removeEmail(e, d){
    $(e.target).closest('.alt-email').remove();
}

function addTips(){
    makeTip('id_alt_email', "Important! Put your gmail or anything you use to send emails to the floor.");
    makeTip('id_password', "Your password will be hashed.");
    makeTip('id_password_confirm',  "We promise.");
    makeTip('id_class_year',  "Graduation year por favor.");
    makeTip('upload',  "Be orginal. Upload your own profile picture!", null, 'hover');
}

$(document).ready(function() {
    $('#upload').click(getImg);
    $('#add-email').click(addEmail)
    $(document).on('click','.remove-email', removeEmail)
    addTips();
});