function addCommprodInput(){
    var template = ' <div><label> <b> Commprod Content: </b> </label><textarea name="commprod" class="commprod input-xlarge"></textarea><a class="btn remove-input remove-commprod"><i class="icon-minus"></i></a></div>';
    $('.commprod').after(template);
}

function removeInput(e, d){
    $(e.target).closest('div').remove();
}

function submitForm(e, d){
    e.preventDefault();
    var $form = $(e.target);
    $form.find('.alert').slideUp();
    $form.find('.btn[type=submit]').button('loading')
    var sender = validateElement($('#email')),
    datetime = validateDatetime($('#datetime')),
    subject = validateElement($('#subject')),
    content = validateElement($('#content')),
    commprods = validateProds($('.commprod')),
    args = [datetime, subject, content, commprods];
    errors = "";
    $.each(args, function(index, obj){
        errors += obj.errors
    });
    if(errors == "") {
        form_data = {}
        form_data[sender.data] = [content.data, commprods.data, datetime.data, subject.data]
        form_data = JSON.stringify(form_data)
        data = {
            'data' : form_data,
            'key' : $key,
        }
        $.post('/commprod/processprod', data, function(res){
            $form.find('.response_text').html("res")
            if (res == 'Success!') {
                var rmClass = "alert-success",
                addClass = "alert-error",
                msg = "Key error";
            } else {
                var rmClass = "alert-error",
                addClass = "alert-success",
                msg = res;
            }

            $form.find('.response_text').html(msg)
            $form.find('.alert').removeClass(rmClass).addClass(addClass).slideDown();
            $form.find('.btn[type=submit]').button('reset')
        });
    } else {
        $form.find('.response_text').html(errors)
        $form.find('.alert').removeClass('alert-success').addClass('alert-error').slideDown();
        $form.find('.btn[type=submit]').button('reset')
    }
}

function validateElement(obj) {
    var errors = "";
    if (obj.val() == "") {
        errors += "<br>No text entered at " + obj.attr('name');
    }

    return {
        'data' : obj.val(),
        'errors' : errors
    }
}

function validateDatetime(obj) {
    var datetime = Date.parse(obj.val()),
    errors = "";
    if (!(datetime instanceof Date)) {
        var errors ="<br>Invalid date"
    } 
    return {
        'data' : datetime,
        'errors' : errors
    }
}

function validateProds(objs) {
    var errors = "",
    prods = []
    $.each(objs, function(index, obj){
        if (obj.value == "") {
            errors += "<br>No text entered at commprod content";
        }
        prods.push(obj.value)
    });
    return {
        'data' : prods,
        'errors' : errors
    }
}

$(function(){
    $key = $("#key").val()
    $('form').find('.alert').slideUp(0);
    $(document).on('click', '.remove-input', removeInput);
    $(document).on('click', '#add-commprod', addCommprodInput);
    $('form').submit(submitForm);
})