from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from notes.models import Notes

def userlogin(rq):
    return render(rq,"login.html")

name ={}
allnotes = {}
def log_in(rq):
    if rq.method == "POST":
        username = rq.POST['username']
        pass1 =  rq.POST['pass']

        user = authenticate(username = username, password = pass1)
        name['user'] = user
        if user is not None:
            login(rq,user)
            note = Notes.objects.filter(userid_id = user.id)
            allnotes['notes'] = note
            return render(rq,"notes.html",allnotes)
        else:
            return render(rq,"login.html")

def notes(rq,id):
    if rq.user.is_anonymous:
        return render(rq,"login.html")
    else:
        note = Notes.objects.filter(userid_id = id)
        allnotes['notes'] = note
        return render(rq,"notes.html",allnotes)

def log_out(rq):
    if rq.method == "POST":
        logout(rq)
        return render(rq,"login.html")


def addnotes(rq):
    if rq.user.is_anonymous:
        return render(rq,"login.html")
    else:
        return render(rq,"addnotes.html",name)

def add_notes(rq,id):
    if rq.method == "POST":
        title = rq.POST['title']
        article = rq.POST['article']
        auther = rq.POST['auther']
        blog = Notes(title = title,article = article,auther = auther, userid_id = id)
        blog.save()
        return redirect('notes',id)

def view_note(rq,id):
    if rq.user.is_anonymous:
        return render(rq,"login.html")
    else:
        note = Notes.objects.filter(id  = id)
        data = {
            'notes' : note
        }
        return render(rq,"viewnotes.html",data)