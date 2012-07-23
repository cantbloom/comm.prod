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

function submitForm(e, d){
	e.preventDefault();
	var $form = $(e.target);
	var id = $(e.target).attr('id');
	$form.find('.btn[type=submit]').button('loading')
	$.post("/edit", $form.serialize(), function(res){
		if (res.success){
			var addClass = "alert-success";
			var removeClass = "alert-error";
			var text = '<p>' + res.success + '</p>';
		} else {
			var addClass = "alert-error";
			var removeClass = "alert-success";
			var text = "";
			for (var i =0, max=res.errors[id].length; i<max; i++){
				text += "<p>" + res.errors[id][i] + "</p>";
			}
		}
		$form.find('.response_text').html(text)
		$form.find('.alert').removeClass(removeClass).addClass(addClass).slideDown();
		$form.find('.btn[type=submit]').button('reset')
	});
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
