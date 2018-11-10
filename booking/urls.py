from django.urls import path
from . import views

app_name = 'booking'
urlpatterns = [
    #/booking/
    path('', views.index, name='index'),

    #/booking/book_indi/
    path('book_indi/', views.book_indi, name='book_indi'),

    #/booking/book_orga/
    path('book_orga/', views.book_orga, name='book_orga'),

    #/booking/con_indi/
    path('con_indi/', views.con_indi, name='con_indi'),

    #/booking/con_orga/
    path('con_orga/', views.con_orga, name='con_orga'),

    #/booking/list_indi/
    path('list_indi/', views.list_indi, name='list_indi'),

    #/booking/list_orga/
    path('list_orga/', views.list_orga, name='list_orga'),

]