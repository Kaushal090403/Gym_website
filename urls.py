
from django.contrib import admin
from django.urls import path
from loapp.views import locate
from app.views import home,update_course,delete_course,about,contact,gallery,list_members,list_memberships,list_trainers,list_members,add_member,update_member,delete_member,add_membership,update_membership,delete_membership,add_trainer,update_trainer,delete_trainer


urlpatterns = [
    path('admin/', admin.site.urls),
    path("locate/",locate, name="locate"),
    path("",home, name="home"),
    path("update_course<int:id>/",update_course, name="update_course"),
    path("delete_course<int:id>/",delete_course, name="delete_course"),
    path("about/",about, name="about"),
    path("contact/",contact, name="contact"),
    path("gallery/",gallery, name="gallery"),
    path("list_memberships/",list_memberships, name="list_memberships"),
    path("list_members/",list_members, name="list_members"),
    path("list_trainers/",list_trainers, name="list_trainers"),
    path("add_member/",add_member, name="add_member"),
    path("update_member<int:id>/",update_member, name="update_member"),
    path("delete_member<int:id>/",delete_member, name="delete_member"),
    path("add_membership/",add_membership, name="add_membership"),
    path("update_membership<int:id>/",update_membership, name="update_membership"),
    path("delete_membership<int:id>/",delete_membership, name="delete_membership"),
    path("add_trainer/",add_trainer, name="add_trainer"),
    path("update_trainer<int:id>/",update_trainer, name="update_trainer"),
    path("delete_trainer<int:id>/",delete_trainer, name="delete_trainer"),

]
