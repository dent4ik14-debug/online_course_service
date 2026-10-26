from django.urls import path
from .views import UsersList, AboutAuthor

app_name = 'users'

urlpatterns = [
    path('', UsersList.as_view(), name='users_list'),
    path('author/<int:pk>/', AboutAuthor.as_view(), name='author_detail'),
]