
from django.urls import path
from . import views

urlpatterns = [
 
    path('bug/register/', views.register_bug, name='register_bug'),
    path('bug/<int:bug_id>/', views.view_bug, name='view_bug'),
    path('bugs/', views.list_bugs, name='list_bugs'),
]
