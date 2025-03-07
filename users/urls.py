from django.urls import path
from users import views


urlpatterns = [
    path('users/signup/', views.UserCreationView.as_view(), name='user-create'),
    path('users/login/', views.login, name='login'),
    path('users/profile/', views.UserProfile.as_view(), name='user-profile'),
]