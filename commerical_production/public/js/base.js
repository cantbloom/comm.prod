function voteSelection (e, data){
	var $src = $(e.srcElement);

	//don't submit again if already selected
	if ($src.hasClass('selected')){
		return; 
	}

	//only select one arrow at a time
	$src.addClass('selected').siblings().removeClass('selected');


	var isUpVote = $src.hasClass('up-vote');
	var score = isUpVote ? 1:-1;

	var id = $src.closest('.up-down-container').data('id'),
	type = $src.closest('.up-down-container').data('type')

	sendVote(id, score, type);
}

function sendVote(id, score, type){
	var $commprod = $('#'+ type + '_object_'  + id);

	var payload = {'id':id, 'score':score, 'type': type};

	$.post('/commprod/vote/', payload, function(res){
		$commprod.trigger('voteResponse', res);
	});
	
	$commprod.trigger('voteSent', payload)
}

function postVote (e, d) {

	var $commprod = $(e.target);

	//change the ui -- to the correct score! remember your diff max!
	var new_score = parseInt($commprod.find('.score').text()) + d.score;
	$commprod.find('.score').html(new_score);

	
}

function openClaimProfile(e, d){
	var $src = $(e.srcElement);
	var user = $src.data('user');


	var $modal = $('#claim-email-modal');
	$modal.find('.replace-email').text(user);
	$modal.data('email',user);

	$modal.modal('show');
}

function submitClaimProfile (e, d) {
	var $modal = $('#claim-email-modal');
	var email = $modal.data('email');
	$.post('/claim_email', {email: email})

	$modal.modal('hide');
}

function submitFeedBack(e, d) {
	$('#submit_success').fadeIn();
	$.post('/feedback', { 
		'feedback' : $('#feedback').val()
	});
	$('#submit_success').fadeOut();
	$('#send-feedback-modal').modal('hide');
	$('#feedback').val("");
}

//filepicker image upload for registration/edit_profile page
function getImg() {
    filepicker.setKey('A1Os2AsKsRgK8t0gbEHcAz')
    filepicker.getFile("image/*",{
        'modal': true, 
        'multiple' : false,
        'services' : filepicker_services(),
        },
        function(url, metadata){
        	$('#pic').find('.btn[type=submit]').removeAttr('disabled').removeClass('disabled');
            $('#profile_pic').attr("src", url);
            $('#id_pic_url').attr("value", url);
        }
     );
}

function dropitemSelected (e, v) {
	$('#search-bar').blur();
	navToUser(v);
}

function navToUser(val){
	var username = user_dict[val];
	window.location = '/users/' + username
}

//Detects if the user is on a mobile browser. Uses helper file lib/mobile_detection.js. Changes filepicker.SERVICES to only facebook and dropbox for mobile
function filepicker_services(){
	if (jQuery.browser.mobile) {
		return [filepicker.SERVICES.FACEBOOK,
    		filepicker.SERVICES.DROPBOX,]
	}
	return [filepicker.SERVICES.WEBCAM,
	    filepicker.SERVICES.COMPUTER,
	    filepicker.SERVICES.FACEBOOK,
	    filepicker.SERVICES.DROPBOX,]
	
}

$(function(){
	$(document).on('click', '.vote-container .vote', voteSelection)

	$(document).on('click', '.claim-profile', openClaimProfile)
	$(document).on('click', '#email-claim-confirm', submitClaimProfile)

	$(document).on('click', '#submit_feedback', submitFeedBack)

	$(document).on('typeaheadItemSelected', dropitemSelected)

	$(document).on('voteSent', postVote)

	$('#search_bar').typeahead({
		'source' : user_list
	});
}); 