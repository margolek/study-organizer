from django.urls import path
from . import views

app_name = 'groups'

urlpatterns =[
	path('',views.ListGroup.as_view(),name='list'),
	path('new/',views.creategroup,name='create'),
	path('<int:pk>/',views.SingleGroup.as_view(),name='detail'),
	path('content/create/',views.create_group_content,name='content_create')
]
