function sendVote(id, score){
	var payload = {'id':id, 'score':score}

	$(document).trigger('voteSent', payload);

	$.post('/vote', payload, function(res){
		console.log(res)
		$(document).trigger('voteResponse', payload)
	});
}

// Fill in auto-complete on search bar
function get_users() {
	$.get('/get_users', function(res){
		user_list = [];
		$.each(res['users'], function(index, user) {
			var name;
			if (user['name'] != " ") {
				name = user['name'];
			} else {
				name = user['username']
			}
			console.log(user)
			user_list.push(name);
		});
		console.log(user_list[0])

		$('#search_bar').typeahead({
			'source' : user_list,
		});
	});
}

$(function(){

	get_users();
	$('.raty-container').raty({
	  half       : true,
	  halfShow   : true,
	  number     : 3,
	  //hints      : ['0', '.5', '1', '1.5', '2', '2.5', '3'],
	  size       : 40,
	  path		 : '/public/img',
	  space      : false,
	  starHalf   : 'bomb-half.png',
	  starOff    : 'bomb-off.png',
	  starOn     : 'bomb-on.png',
	  score : function() {
	  	return $(this).attr('data-rating');
	  },
	  click : function(score, evt) {
	    //send to server
	    sendVote($(this).attr('data-id'), score)
	  }
	});
}); 