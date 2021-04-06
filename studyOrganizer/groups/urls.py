from django.urls import path
from . import views

app_name = 'groups'

urlpatterns =[
	path('',views.ListGroup.as_view(),name='list'),
	path('new/',views.creategroup,name='create'),
	path('<int:pk>/',views.SingleGroup.as_view(),name='detail'),
	path('<int:pk>/content/create/',views.create_group_content,name='content_create'),
	# path('<int:pk>/content/<int:post_id>/update/',views.GroupContentUpdate.as_view(),name='content_update'),
	# path('content/<int:pk>/delete/',views.GroupContentDelete.as_view(),name='content_delete')
]
