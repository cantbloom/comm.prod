function insertCommprod(e, d){
	var toAdd = $(data.commprods.shift());
	
	toAdd.hide();
	toAdd.css('opacity', 0);
	
	$(e.currentTarget).prepend(toAdd);
	
	toAdd.slideDown(function(){
		toAdd.animate({opacity:1}, 150);
	});

	if (data.commprods.length < 20){
		$.getJSON('/commprod/api/search', {unread:true, limit:10, return_type:'list'}, function(res){
			data.commprods = data.commprods.concat(res.res);
			console.log(data.commprods.length)
		})
	}
}

$(function(){
	var $commprod_timeline = $('.commprod-timeline');

	$commprod_timeline.on('needsCommprod voteSent', insertCommprod)

	$commprod_timeline.trigger('needsCommprod');
})