from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
	path('<slug:slug>/new/',views.create_content,name='create'),
	path('<int:pk>',views.content_detail,name='detail'),
	path('<slug:slug>/<int:pk>/update',views.ContentUpdate.as_view(),name='update'),
	path('<slug:slug>/<int:pk>/delete',views.ContentDelete.as_view(),name='delete'),
]