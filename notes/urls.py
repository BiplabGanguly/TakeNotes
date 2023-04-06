from django.contrib import admin
from django.urls import path
from notes import views

urlpatterns = [
    path('',views.userlogin,name="login"),
    path('login/',views.log_in,name="loginuser"),
    path('addnotes/',views.addnotes,name="addnotes"),
    path('add_notes/<id>/',views.add_notes,name="add_notes"),
    path('logput/',views.log_out,name="logout"),
    path('viewnotes/<id>',views.view_note,name="viewnote"),
    path('notes/<id>',views.notes,name="notes"),
]