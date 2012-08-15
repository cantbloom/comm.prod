(function(window, undefined){
    var typeKeys = [67, 65, 78, 84, 66, 76, 79, 79, 77],
    something_index = 0,
    handler = function(e) {
    if (e.keyCode === typeKeys[something_index++]) {
      if (something_index === typeKeys.length) {
        $(document).unbind("keydown", handler);
        complete();
      }
    } else {
      something_index = 0;
    }
    };

    $(document).bind("keydown", handler);
})(this);

function complete(){
    $.getScript("/public/js/aster.js", function(data, status){});
}

$(function(){
    $(document).bind("complete_rec", complete)
});