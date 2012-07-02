function sendVote(id, score){
	var payload = {'id':id, 'score':score}

	$(document).trigger('voteSent', payload);

	$.post('/vote', payload, function(res){
		$('#commprod_'+res.cp_id).trigger('voteResponse', res);
	});
}

function updateAvgScore(e, data){
	if (data.success){
		var $commprod = $('#commprod_'+data.cp_id)

		//update 
		$commprod.find('.score').html(data.avg_score.toFixed(2));

		//make sure personal score set correctly
		$commprod.find('.raty-container').raty('set', { score:data.score});
	}
}

$(function(){
	$(document).on('voteResponse', updateAvgScore);

	$('#search_bar').typeahead({
			'source' : user_list,
		});

	$('.raty-container').raty({
	  half       : true,
	  halfShow   : true,
	  number     : 3,
	  //hints      : ['0', '.5', '1', '1.5', '2', '2.5', '3'],
	  size       : 32,
	  path		 : '/public/img',
	  space      : false,
	  starHalf   : 'bomb-half.png',
	  starOff    : 'bomb-off.png',
	  starOn     : 'bomb-on.png',
	  score : function() {
	  	return parseFloat($(this).attr('data-rating')).toFixed(2);
	  },
	  click : function(score, evt) {
	    //send to server
	    sendVote($(this).attr('data-id'), score)
	  }
	});
}); 