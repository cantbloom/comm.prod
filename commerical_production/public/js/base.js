function voteSelection (e, data){
    var $src = $(e.target);
    var $commprod = $src.closest('.commprod-container');
    //don't submit again if already selected
    if ($src.hasClass('selected')){
        return; 
    }

    //gather info about this vote
    var isUpVote = $src.hasClass('up-vote');
    var score = isUpVote ? 1:-1;
    var id = $commprod.data('id'),
    type = $commprod.data('type');

    //diff is the change from this users previous score given to this commprod
    var diff = $commprod.find('.vote').hasClass('selected') ? score*2 : score;

    //only select one arrow at a time
    $src.addClass('selected').siblings().removeClass('selected');
    sendVote(id, score, type, diff);
}

function sendVote(id, score, type, diff){
    var $commprod = $('#'+ type + '_object_'  + id);

    var payload = {'id':id, 'score':score, 'type': type, 'diff':diff};

    $.post('/commprod/vote/', payload, function(res){
        $commprod.trigger('voteResponse', res);
    });
    
    $commprod.trigger('voteSent', payload)
}

function openClaimProfile(e, d){
    var $src = $(e.target);
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

function postVote (e, d) {
    var $commprod = $(e.target);

    //quickly change the ui -- must use diff to handle if user already voted
    var new_score = parseInt($commprod.find('.score').text()) + d.diff;
    $commprod.find('.score').html(new_score);

    /*
    Below is correction only stuff
    */
    if ($commprod.data('type') != 'correction'){
        return;
    }
    //note the below code probably only work for the permalink page. Be careful expecting this to work elsewhere
    var max = 5;
    var min = -5;

    var new_score = $commprod.find('.score').text()

    if (new_score>=max) {
        //make new_prod the features one.
        var new_prod = $commprod.find('.commprod-content').html();
        $('.commprod-content:first').html(new_prod);

        //remove all other commprod
        $('.correction').remove();
   }
   else if (new_score<=min) {
        $commprod.remove();
   }
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

function detailsCorrectionText(e, v) {
    $(e.target).text("Click for more")
}

function detailsDefaultText(e, v) {
    $(e.target).text("Details")
}

function submitForm(e, d){
    e.preventDefault();
    var $form = $(e.target);
    var id = $form.attr('id');
    var url = $form.data('url')
    $form.find('.btn[type=submit]').button('loading')
    $.post(url, $form.serialize(), function(res){
        if (res.success){
            var addClass = "alert-success";
            var removeClass = "alert-error";
            var text = '<p>' + res.success + '</p>';
        } else {
            var addClass = "alert-error";
            var removeClass = "alert-success";
            var text = "";
            for (var i =0, max=res.errors[id].length; i<max; i++){
                text += "<p>" + res.errors[id][i] + "</p>";
            }
        }
        $form.find('.response_text').html(text)
        $form.find('.alert').removeClass(removeClass).addClass(addClass).slideDown();
        $form.find('.btn[type=submit]').button('reset')
    });
}



$(function(){
    $(document).on('click', '.vote-container .vote', voteSelection)
    $('.permalink').hover(detailsCorrectionText, detailsDefaultText)
    $('.permalink').popover()
    $(document).on('click', '.claim-profile', openClaimProfile)
    $(document).on('click', '#email-claim-confirm', submitClaimProfile)

    $(document).on('click', '#submit_feedback', submitFeedBack)

    $(document).on('typeaheadItemSelected', dropitemSelected)

    $(document).on('voteSent', postVote);

    $('#search_bar').typeahead({
        'source' : user_list
    });
}); 
