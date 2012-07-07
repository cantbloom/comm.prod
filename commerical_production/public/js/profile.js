$('#raty').raty({
    half : true,
    precision : true,
    readOnly : true,
    halfShow : true,
    number : 3,
    noRatedMsg : "",
    target : '#target',
    targetType : 'number',
    targetFormat : '{score}',
    targetText : 'none',
    targetKeep : true,
    size : 32,
    path : '/public/img',
    space : false,
    starHalf : 'bomb-half.png',
    starOff : 'bomb-off.png',
    starOn : 'bomb-on.png',
    score : function() {
        return parseFloat($(this).attr('data-rating')/10).toFixed(2);
    },
});

function get_vs_data(filter) {
    var url = '/commprod/api/vs_data';
    if (filter) {
        url += '?filter=' + filter
    }
    $.get(url, function(data){
        console.log(data);
    })
}

$(function(){
    get_vs_data();
}); 
