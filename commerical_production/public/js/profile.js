$(function(){

    //initialize rating on top div.
    $('#raty').raty({
        half : true,
        precision : true,
        readOnly : true,
        halfShow : true,
        number : 3,
        noRatedMsg : "",
        size : 32,
        path : '/public/img',
        space : false,
        starHalf : 'bomb-half.png',
        starOff : 'bomb-off.png',
        starOn : 'bomb-on.png',
        score : function() {
            return parseFloat($(this).attr('data-rating')/10).toFixed(2); // normalize rating to scale
        },
    });
    $('.tab').click(tabListener);
    $('#vs_class_tab').trigger('click');


}); 


//Default event listener clears active tabs,
//Places active class on tab that was clicked,
//Calls respective graphing function.
function tabListener(){
    clearActiveTabs();
    $(this).attr('class', 'active');//set tab to active
    var id = $(this).attr('id'),
    tab = id.slice(0, id.length -4);
    if (id == 'trends_tab') {

    }
    else {
        var filter = $(this).data('classYear');
        getVsData(filter, tab);
    }
}

//clear classes on tabs
function clearActiveTabs() {
    var tabs = ['#vs_class_tab', '#vs_floor_tab', '#trends_tab'];
    $.each(tabs, function(index, tab){
        $(tab).attr('class', '');
    });
}

//calls api for vs_data
//renders new graph and puts
//mean and std of data on page
function getVsData(filter, tab) {
    var username = $('#username').data('username'),
    url = '/commprod/api/vs_data?username=' + username;
    if (filter) {
        url += '&?filter=' + filter; 
    }
    $('#chart_container').empty(); //clear old graph
    $.get(url, function(vs_data){
        renderVsGraph(vs_data['data_points'], tab);
        $('#std').text(vs_data['std'].toFixed(2));
        $('#mean').text(vs_data['mean'].toFixed(2));
        $('#grade').text(vs_data['grade']);
    })
}

//create new graph for vs_data
function renderVsGraph(data_points, tab) {
    var title = $('#' + tab).text();
    var chart = new Highcharts.Chart({
        chart : {
            renderTo: 'chart_container',
            type: 'column'
        },
        colors : ['#fe7227'],
        title : {
            text: title
        },
        yAxis : {
            title : {
                text : "Number of users",
            },
        },
        xAxis : {
            type : 'linear',
            title : {
                text : "Avg User Score",
            },
        },
        tooltip: {
            formatter: function() {
                return ''+
                    this.series.name +': '+ this.y +'';
            }
        },

        credits : {
            enabled: false,
        },

        series : [{
            name : "Number of users",
            data: data_points,
        }],
        exporting : {
            enabled : false,
        }
    });
}