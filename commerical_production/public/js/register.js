$(document).ready(function() {
    $('#upload').click(getImg);
    addTips();
});
 

function getImg() {
    filepicker.setKey('A1Os2AsKsRgK8t0gbEHcAz')
    filepicker.getFile("image/*", 
    {
        'modal': true, 
        'multiple' : false,
        'services' : [filepicker.SERVICES.WEBCAM,
                    filepicker.SERVICES.COMPUTER,
                    filepicker.SERVICES.FACEBOOK,
                    filepicker.SERVICES.DROPBOX,]
        },
         function(url, metadata){
            url += "/resize?w=40&h=40"; //image resize:
            $('#profile_pic').attr("src", url);
            $('#id_pic_url').attr("value", url);
         }
     );
}

function addTips(){
    makeTip('id_alt_email', "Important! Put your gmail or anything you use to send emails to the floor.");
    makeTip('id_shirt_name', 'Be Honest :)');
    makeTip('id_password', "Your password will be encrypted.");
    makeTip('id_password_confirm',  "We promise.");
    makeTip('upload',  "Be orginal. Upload your own profile picture!", null, 'hover');
}

//defaults to placing right and focus trigger if 
//no values given.
function makeTip(div,title, placement, trigger) {
    placement = placement || 'right';
    trigger = trigger || 'focus'
    $('#' + div).tooltip({
        "placement" : placement,
        "title" : title,
        "trigger" : trigger,
    });
}