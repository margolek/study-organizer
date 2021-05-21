from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create_polls, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.PollUpdate.as_view(), name='edit'),
    path('<int:pk>/edit/add_choice', views.add_choice, name='add_choice'),
    # path('<int:choice_pk>/change_choice', views.ChoiceUpdate.as_view(), name='change_question'),
    path('<int:pk>/delete/', views.PollDelete.as_view(), name='delete'),
    path('<int:pk>/results/', views.results, name='results'),
    path('<int:pk>/vote/', views.vote, name='vote'),
    path('resultsdata/<str:obj>/', views.resultsData, name="resultsdata"),
]