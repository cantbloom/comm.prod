function voteSelection (e, data){
	var $src = $(e.srcElement);
	$src.addClass('selected').siblings().removeClass('selected');


	var isUpVote = $src.hasClass('up-vate');
	var score = isUpVote ? 1:-1;

	var id = $src.closest('.up-down-container').attr('data-id');

	sendVote(id, score);
}

function sendVote(id, score){
	var payload = {'id':id, 'score':score}

	$.post('/vote', payload, function(res){
		$('#commprod_'+res.cp_id).trigger('voteResponse', res);
	});

	$('#commprod_'+id).trigger('voteSent', payload)
}

function updateAvgScore(e, data){
	if (data.success){
		var $commprod = $('#commprod_'+data.cp_id)

		//not udpating now because of lag...//update 
		//$commprod.find('.score').html(data.avg_score.toFixed(2));

		//todo:
		//make sure psonal score set correctly
	}
}






$(function(){
	$(document).on('voteResponse', updateAvgScore);
	$(document).on('click', '.vote-container span', voteSelection)
}); 