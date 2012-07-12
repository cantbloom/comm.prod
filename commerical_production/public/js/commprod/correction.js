$(function(){
    //check for illegal text
    $('#submit_correction').click(function() {
        var check_text = $('#corrected_text').val().toLowerCase();
        if (check_text.indexOf("btb") != -1 || check_text.indexOf("comm") != -1 || check_text.indexOf("prod") != -1) {
            $('#submit_warning').slideDown()
        } else{
            submit_correction();
        }
    });

    //send post request
    $('#submit_checked').click(submit_correction);
    //hide warning
    $('#edit_again').click(function() {
        $('#submit_warning').hide();
    });
    //hide warning
    $('#corrected_text').bind('keyup', function(){
         $('#submit_warning').slideUp();
    });
});

function submit_correction() {
    var content = $('#corrected_text').val()
    payload = {
        'content' : content, 
        'cp_id' : commprod_data['cp_id'],
        'user' : commprod_data['username']
    };

    $.post('/commprod/correction', payload, function(res){
        $('#correction_container').append(res['correction'][0]);
        $('#submit_success').slideUp();
    });
    $('#correction_modal').modal('hide');
    $('#submit_success').slideDown();
}
