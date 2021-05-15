from django.urls import path
from .import views

app_name = 'groups'

urlpatterns =[
	path('',views.ListGroup.as_view(),name='list'),
	path('new/',views.creategroup,name='create'),
	path('<slug:slug>/',views.SingleGroup.as_view(),name='detail'),
	path('join/<slug:slug>/',views.JoinGroup.as_view(),name='join'),
	path('leave/<slug:slug>/',views.LeaveGroup.as_view(),name='leave'),
]
