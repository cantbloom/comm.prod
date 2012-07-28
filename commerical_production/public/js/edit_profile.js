function removeInput(e, d){
    $(e.srcElement).closest('p').remove();
}

function addShirtNameInput(){
	var template = '<p><input type="text" class="removable_input" placeholder="Shirt name" name="shirt_name"><a class="btn remove-input remove-shirt-name"><i class="icon-minus"></i></a></p>'
	$('#add-shirt-name').closest('p').before(template);
}

function addEmailInput(){
	var template = '<p><input type="email" class="removable_input" placeholder="Alternate email" name="email"><a class="btn remove-input remove-shirt-name"><i class="icon-minus"></i></a></p>'
	$('#add-email').closest('p').before(template);
}

function toggleAccordion (e, d){
	var $accordion = $(e.target).closest('.accordion-group');

	var $arrow = $accordion.find('.arrow');

	$arrow.toggleClass('icon-chevron-down');
	$arrow.toggleClass('icon-chevron-up');
}


$(function(){
	$(".collapse").collapse()
	$('form').find('.alert').slideUp(0);

    $('#upload').click(getImg);
	$('form').submit(submitForm);

	$(document).on('click', '.remove-input', removeInput);
	$(document).on('click', '#add-shirt-name', addShirtNameInput);
	$(document).on('click', '#add-email', addEmailInput);
	
	$('#add-email').click()
	$('#add-shirt-name').click()
	
	$(document).on('show hide', '.accordion-body', toggleAccordion)
});
