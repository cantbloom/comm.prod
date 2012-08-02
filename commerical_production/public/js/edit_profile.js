function removeInput(e, d){
    $(e.target).closest('p').remove();
}

function addShirtNameInput(){
	var template = '<p><input type="text" class="removable_input" placeholder="Shirt name" name="shirt_name"><a class="btn remove-input remove-shirt-name"><i class="icon-minus"></i></a></p>'
	$('#add-shirt-name').closest('p').before(template);
}

function addEmailInput(){
	var template = '<p><input type="email" class="removable_input" placeholder="Alternate email" name="email"><a class="btn remove-input remove-shirt-name"><i class="icon-minus"></i></a></p>'
	$('#add-email').closest('p').before(template);
}

function switchTab(e, d) {
	$('.tab').closest('li').removeClass("active");
	$(e.target).closest('li').addClass("active");
	var id = $(e.currentTarget).attr('id').split("-")[0];
	$('form').addClass('hidden');
	$('#' + id).removeClass('hidden');
	$('form').find('.alert').slideUp(0)
}

$(function(){
	$('.tab').click(switchTab);;

    $('#upload').click(getImg);
	$('form').submit(submitForm);
	$(document).on('click', '.remove-input', removeInput);
	$(document).on('click', '#add-shirt-name', addShirtNameInput);
	$(document).on('click', '#add-email', addEmailInput);
	
	$('#add-email').click();
	$('#add-shirt-name').click();
	$('#pic-tab').click();

});
