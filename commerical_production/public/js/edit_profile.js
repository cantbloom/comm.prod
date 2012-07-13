function removeInput(e, d){
    $(e.srcElement).closest('p').remove();
}

function addShirtNameInput(){
	var template = '<p><input type="text" class="removable_input" placeholder="Shirt name" name="shirt_name"><a class="btn remove-input remove-shirt-name"><i class="icon-minus"></i></a></p>'
	$('#add-shirt-name').closest('p').before(template);
}

function addEmailInput(){
	var template = '<p><input type="text" class="removable_input" placeholder="Alternate email" name="email"><a class="btn remove-input remove-shirt-name"><i class="icon-minus"></i></a></p>'
	$('#add-email').closest('p').before(template);
}

function submitForm(e, d){
	e.preventDefault();
	
	var $form = $(e.target);
	var id = $(e.target).attr('id');
	$.post("/edit", $form.serialize(), function(res){
		if (res.success){
			var addClass = "alert-success";
			var removeClass = "alert-error";
			var text = res.success;
		} else {
			var addClass = "alert-error";
			var removeClass = "alert-success";
			var text = "<ul>";
			for (var i =0, max=res.errors[id].length; i<max; i++){
				text += "<li>" + res.errors[id][i] + "</li>";
			}
			text+= "</ul>";
		}

		$form.find('.alert').removeClass(removeClass).addClass(addClass).html(text).slideDown();
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

	$(document).on('show hide', '.accordion-body', toggleAccordion)
});
