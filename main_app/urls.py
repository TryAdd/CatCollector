from django.urls import path
from . import views


urlpatterns = [
    #? Routes in express, url in django
    path('', views.home, name='home'), 

     #? about 
    path('about/', views.about ,name ='about'),

    #? for Cats
    path('cats/', views.cats_index, name='index'),

    #? for details
    path('cats/<int:cat_id>', views.cats_detail, name='detail'),

    #? for cats create
    path('cats/create/', views.CatCreate.as_view(), name='cats_create'),

    #? for update
    path('cats/<int:pk>/update', views.CatUpdate.as_view(), name='cats_update'),

    #? for delete
    path('cats/<int:pk>/delete', views.CatDelete.as_view(), name='cats_delete'),

    #? for feeding 
    path('cats/<int:cat_id>/add_feeding', views.add_feeding, name='add_feeding'),

    #? for toys
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    
    #? for toys detail
    path('toys/<int:pk>', views.ToyDetail.as_view(), name='toys_detail'),
    
    #? for toys create
    path('toys/create', views.ToyCreate.as_view(), name='toys_create'),
    
    #? for toys update
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    
    #? for toys delete
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
    
    #? for assosiate a toy with a cat m/m
    path('cat/<int:cat_id>/assoc_toy/<int:toy_id>', views.assoc_toy, name='assoc_toy'),
    
    #? for unassosiate a toy with a cat m/m
    path('cat/<int:cat_id>/unassoc_toy/<int:toy_id>', views.unassoc_toy, name='unassoc_toy'),
    
    #? for our signup
    path('accounts/signup', views.signup, name='signup'),

]