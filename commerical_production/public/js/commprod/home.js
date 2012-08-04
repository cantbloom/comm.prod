function insertCommprod(e, d){
	var $toAdd = $(data.commprods.shift());

	$toAdd.addClass('first');
	$toAdd.hide();
	$toAdd.css('opacity', 0);

	$(e.currentTarget).find('.first').removeClass('first');
	$(e.currentTarget).prepend($toAdd);

	$toAdd.slideDown(function(){
		$toAdd.animate({opacity:1}, 150);
	});

	if (data.commprods.length < 10){
		requestProds();
	}

	//add popover since this commprod wasn';'t arround when it was first added
	$toAdd.find('.permalink').hover(detailsCorrectionText, detailsDefaultText).popover()

}

function requestProds(cb){
	$.getJSON('/commprod/api/search', {unvoted:true, limit:15, orderBy: '?', return_type:'list'}, function(res){
			data.commprods = data.commprods.concat(res.res);
			if (cb){
				cb(res);
			}
	});
    $(document).trigger('requestMoreProds', {loc: 'home'});
}

function setupTour(){
	tour = new Tour(
		{
			afterSetState : function(k,e){
				if (k == "end" && e=="yes"){
					$(document).trigger('tourEnded', {current:tour._current})
				}
			}
		}
	)


	tour.addStep({
	  element: ".commprod-timeline-container h1", /* html element next to which the step popover should be shown */
	  placement: 'bottom',
	  title: "Home", /* title of the popover */
	  content: "On the home page, you see comm.prods that you haven't voted on yet.", /* content of the popover */

	  onShow: function(tour){
	  	$(document).trigger('toolTipShow', {type:'home'})
	  }
	});

	tour.addStep({
	  element: ".up-down-container:first", /* html element next to which the step popover should be shown */
	  placement: 'bottom',
	  title: "Voting", /* title of the popover */
	  content: "Use these buttons to vote. Once you place a vote another comm.prod will slide in." , /* content of the popover */
	  onShow: function(){
	  	$(document).trigger('toolTipShow', {type:'voting'})
	  }
	});

	tour.addStep({
	  element: ".date:first", /* html element next to which the step popover should be shown */
	  placement: 'bottom',
	  title: "Details", /* title of the popover */

	  content: "Hover over this link and you'll see the email it was in. Click it to go to a page where you can see other comm.prods from the email and submit corrections.", /* content of the popover */
	  onShow: function(){
	  	$(document).trigger('toolTipShow', {type:'details'})
	  }
	});

	tour.addStep({
	  element: ".author-container:first", /* html element next to which the step popover should be shown */
	  placement: 'left',
	  title: "Profiles", /* title of the popover */
	  content: "Click the name or photo to be taken to that user's profile page", /* content of the popover */
	  onShow: function(){
	  	$(document).trigger('toolTipShow', {type:'profiles'})
	  }
	});

	tour.addStep({
	  element: ".search-nav .nav:visible", /* html element next to which the step popover should be shown */
	  placement: 'bottom',
	  title: "Other Pages", /* title of the popover */
	  content: "Use these links to change how comm.prods are ordered.", /* content of the popover */
	  onShow: function(){
	  	$(document).trigger('toolTipShow', {type:'other pages'})
	  }
	});



	tour.start();
}

$(function(){
	setupTour();

	var $commprod_timeline = $('.commprod-timeline');

	$commprod_timeline.on('needsCommprod', insertCommprod)

	$commprod_timeline.on('voteSent', function(e, d){
		//ignore if clicked on a commprod that isn't first
		if (!$(e.target).is('.commprod-container.first')){
			return;
		}

		$commprod_timeline.trigger('needsCommprod');
	});

	requestProds(function(){
		$('.commprod-timeline .loading').hide();
		$commprod_timeline.trigger('needsCommprod');	
	});
})