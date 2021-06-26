from django.urls import path
from .import views

app_name = 'groups'

urlpatterns =[
	path('',views.ListGroup.as_view(),name='list'),
	path('new/',views.creategroup,name='create'),
	path('<slug:slug>/',views.SingleGroup.as_view(),name='detail'),
	path('send-request/<slug:slug>/',views.SendGroupRequest.as_view(),name='join'),
	path('cancel-request/<slug:slug>/',views.CancelGroupRequest.as_view(),name='cancel'),
	path('accept-request/<slug:slug>/',views.AcceptGroupRequest.as_view(),name='accept'),
	path('reject-request/<slug:slug>/',views.RejectGroupRequest.as_view(),name='reject'),
	path('leave/<slug:slug>/',views.LeaveGroup.as_view(),name='leave'),
]
