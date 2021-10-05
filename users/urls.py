from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('login/' , views.user_login , name="login"),
    path('signup/' , views.user_register , name="signup"),
    path('logout/' , views.user_logout , name="logout"),
    path('profile/<int:pk>/<str:username>/' , views.user_profile, name="profile"),
    path('profile/edit-profile/<str:username>/' , views.edit_profile, name="edit_profile"),
    path('login/phone/' , views.phone_login, name="phone_login"),
]