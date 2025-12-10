from django.urls import path
from .views import dashboard,catogories,add_category,edit_category,delete_category

urlpatterns=[
    path('',dashboard,name='dashboard'),
    path('categories/',catogories,name='categories'),
    path('categories/add/',add_category,name='add_category'),
    path('categories/add/edit/<int:pk>/',edit_category,name='edit_category'),
     path('categories/add/delete/<int:pk>/',delete_category,name='delete_category')
]