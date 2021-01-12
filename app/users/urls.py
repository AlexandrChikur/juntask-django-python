from django.urls import path, include

from .views import UsersListView, UserDetailView



urlpatterns = [
    path('users/', UsersListView.as_view()),
    path('users/<str:pk>/', UserDetailView.as_view()),
]
