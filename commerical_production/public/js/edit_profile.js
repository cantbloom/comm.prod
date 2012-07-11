$(function(){
	$(".collapse").collapse()
	$(document).on('click', '.remove-input', removeInput);
	$(document).on('click', '#add-shirt-name', addShirtNameInput);
	$(document).on('click', '#add-email', addSEmailInput);
});


function removeInput(e, d){
    $(e.srcElement).closest('p').remove();
}

function addShirtNameInput(){
	var template = '<p><input type="text" class="removable_input" placeholder="Shirt name" name="shirt_name"><a class="btn remove-input remove-shirt-name"><i class="icon-minus"></i></a></p>'
	$('#shirt-name-save').before(template);
}

function addSEmailInput(){
	var template = '<p><input type="text" class="removable_input" placeholder="Alternate email" name="alt_email"><a class="btn remove-input remove-shirt-name"><i class="icon-minus"></i></a></p>'
	$('#shirt-name-save').before(template);
}