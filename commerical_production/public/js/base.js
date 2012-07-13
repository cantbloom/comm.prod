function voteSelection (e, data){
	var $src = $(e.srcElement);

	if ($src.hasClass('selected')){
		return;
	}
	$src.addClass('selected').siblings().removeClass('selected');


	var isUpVote = $src.hasClass('up-vote');
	var score = isUpVote ? 1:-1;

	var id = $src.closest('.up-down-container').data('id'),
	type = $src.closest('.up-down-container').data('type')
	sendVote(id, score, type);
}

function sendVote(id, score, type){
	var payload = {'id':id, 'score':score},
	url = '/commprod/vote/'
	if (type == 'correction') {
		url += type;
	} else {
		url += 'commprod'
		type = 'commprod';
	}
	$.post(url, payload, function(res){
		var div_id = '#'+ type + '_object_'  + res.id;
		res['type'] = type
		$(div_id).trigger('voteResponse', res);
		if (res.rm_all == true) {
			var new_prod = $(div_id +'_content').html();
			$('.commprod-content:first').html(new_prod);
			$('.correction').remove();
		}
		else if (res.rm == true) {
			$(div_id).remove();
		}
	});
	$('#'+ type + '_object_' + id).trigger('voteSent', payload)
}

function updateAvgScore(e, data){
	if (data.success){
		var $commprod = $('#'+ data.type + '_object_'+ data.cp_id);

		//not udpating now because of lag...//update 
		//$commprod.find('.score').html(data.avg_score.toFixed(2));

		//todo:
		//make sure psonal score set correctly
	}
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
        'services' : [filepicker.SERVICES.WEBCAM,
                    filepicker.SERVICES.COMPUTER,
                    filepicker.SERVICES.FACEBOOK,
                    filepicker.SERVICES.DROPBOX,]
        },
        function(url, metadata){
        	$('#pic').find('.btn[type=submit]').removeAttr('disabled').removeClass('disabled');
            $('#profile_pic').attr("src", url);
            $('#id_pic_url').attr("value", url);
        }
     );
}

$(function(){
	$(document).on('voteResponse', updateAvgScore);

	$(document).on('click', '.vote-container div', voteSelection)

	$(document).on('click', '.claim-profile', openClaimProfile)
	$(document).on('click', '#email-claim-confirm', submitClaimProfile)

	$(document).on('click', '#submit_feedback', submitFeedBack)

	$('#search_bar').typeahead({
		'source' : user_list
	});
}); 