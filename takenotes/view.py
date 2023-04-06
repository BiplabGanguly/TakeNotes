from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
def website(rq):
    return render(rq,"index.html")

def usersign(rq):
    return render(rq,"signin.html")

er = {}
def createuser(rq):
    if rq.method == "POST":
        username = rq.POST['username']
        pass1 = rq.POST['pass1']
        pass2 = rq.POST['pass2']

        if pass1 == pass2:
            user = User.objects.create_user(username = username, password= pass1)
            user.save()
            er['message'] = "User create successfull!!"
            return render(rq,"index.html",er)
        

