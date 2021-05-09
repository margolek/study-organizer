from django.urls import path
from .import views

app_name = 'groups'

urlpatterns =[
	path('',views.ListGroup.as_view(),name='list'),
	path('new/',views.creategroup,name='create'),
	path('<slug:slug>/',views.SingleGroup.as_view(),name='detail'),
]
