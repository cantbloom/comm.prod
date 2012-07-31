$(function(){
	$(document).on('voteSent', function(e, d){
		d.location = window.location.pathname;
		seg.track('Voted on a ' + d.type , d);
	});

	$(document).on('profileTab', function(e, d){
		seg.track('Changed tab to ' + d.id , d);
	});

	$(document).on('profileVisit', function(e, d){
		seg.track('Visited profile', d);
	});

	$(document).on('myProfileVisit', function(e, d){
		seg.track('Visited own profile', d);
	});
});