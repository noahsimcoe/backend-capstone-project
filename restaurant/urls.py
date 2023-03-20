from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index")
]


#urlpatterns = [
#    path("", views.home, name="home"),
#    path("about/", views.about, name="about"),
#    path("book/", views.books, name="book"),
#    path("menu/", views.menu, name="menu"),
#    path("menu_item/<int:pk>/", views.display_menu_item, name="menu_item")
#],

# the paths are binded to certain views that will be loaded in

