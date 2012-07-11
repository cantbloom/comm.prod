function insertCommprod(e, d){
	var toAdd = $(data.commprods.shift());
	
	toAdd.addClass('first');
	toAdd.hide();
	toAdd.css('opacity', 0);
	
	$(e.currentTarget).find('.first').removeClass('first');
	$(e.currentTarget).prepend(toAdd);
	
	toAdd.slideDown(function(){
		toAdd.animate({opacity:1}, 150);
	});

	if (data.commprods.length < 20){
		$.getJSON('/commprod/api/search', {unread:true, limit:10, return_type:'list'}, function(res){
			data.commprods = data.commprods.concat(res.res);
		});
	}
}

$(function(){
	var $commprod_timeline = $('.commprod-timeline');

	$commprod_timeline.on('needsCommprod', insertCommprod)

	$commprod_timeline.on('voteSent', function(e, d){
		//ignore if clicked on a commprod that isn't first
		if (!$(e.target).is('.commprod-container.first')){
			return;
		} 

		$commprod_timeline.trigger('needsCommprod');		
	});

	$commprod_timeline.trigger('needsCommprod');
})