from commProd.models import UserProfile
import os

def update():
    print "Updating user list..."
    path = os.path.abspath(os.path.join('commerical_production/public/js/', os.path.pardir))
    path += "/js/user_list.js"
    profiles = UserProfile.objects.all().select_related()
    user_list = []
    user_dict = {}
    for profile in profiles:
        username = profile.user.username
        name = profile.user.first_name + " " + profile.user.last_name
        if name == " ":
            name = profile.user.username
        user_dict[str(name)] = str(username)
        user_list.append(str(name))
        print "Added", name
    data = "var user_list = " + str(user_list)
    data += "\nvar user_dict =" + str(user_dict)
    f = open(path, 'w')
    f.write(data)
    f.close()
    print "Complete"

