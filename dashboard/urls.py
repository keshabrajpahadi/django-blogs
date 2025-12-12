from django.urls import path
from .views import dashboard,catogories,add_category,edit_category,delete_category,posts,add_post,edit_post,delete_post,users,edit_user,add_user
urlpatterns=[
    path('',dashboard,name='dashboard'),
    #categories 
    path('categories/',catogories,name='categories'),
    path('categories/add/',add_category,name='add_category'),
    path('categories/add/edit/<int:pk>/',edit_category,name='edit_category'),
     path('categories/add/delete/<int:pk>/',delete_category,name='delete_category'),
     # blog post 
     path('posts/',posts,name='posts'),
      path('posts/add/',add_post,name='add_post'),
    path('posts/edit/<int:pk>/',edit_post,name='edit_post'),
     path('posts/delete/<int:pk>/',delete_post,name='delete_post'),
     ##users
     path('users',users,name='users'),
     path('users/add/',add_user,name='add_user'),
     path('users/edit/',edit_user,name='edit_user')

]