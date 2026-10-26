from django.urls import path
from .views import UsersList, AboutAuthor, CustomLoginView, CustomRegistrationView, ProfileView
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('', UsersList.as_view(), name='users_list'),
    path('author/<int:pk>/', AboutAuthor.as_view(), name='author_detail'),
    path('register/', CustomRegistrationView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile')
]