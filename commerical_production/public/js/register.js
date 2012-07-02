$(document).ready(function() {
    addTips();
    $('#upload').click(getImg);
});
 

function getImg() {

     //Seting up Filepicker.io with your api key
    filepicker.setKey('A1Os2AsKsRgK8t0gbEHcAz');
     //Get your first file - How exciting!
     //This call asks for any type of file, and makes an alert window stating
     //the name of the file and where to download it from.
    filepicker.getFile("image/*", 
        {
        'modal': true, 
        'multiple' : false,
        'services' : [filepicker.SERVICES.WEBCAM,
                    filepicker.SERVICES.COMPUTER,
                    filepicker.SERVICES.FACEBOOK,
                    filepicker.SERVICES.DROPBOX,
                    ]
        },
         function(url, metadata){
             $('#id_pic_url').attr("value", url);
         }
     );
}

function addTips(){
    $('#id_alt_email').tooltip({
        "placement" : "right",
        "title" : "Important! Put your gmail or anything you use to send emails to the floor.",
        "trigger" : "focus"
    });

    $('#id_shirt_name').tooltip({
        "placement" : "right",
        "title" : "Be Honest :)",
        "trigger" : "focus"
    });

    $('#id_password').tooltip({
        "placement" : "right",
        "title" : "Your password will be encrypted.",
        "trigger" : "focus"
    });

    $('#id_password_confirm').tooltip({
        "placement" : "right",
        "title" : "We promise.",
        "trigger" : "focus"
    });

    $('#upload').tooltip({
        "placement" : "right",
        "title" : "Be orginal. Upload your own profile picture!",
        "trigger" : "hover"
    });
}