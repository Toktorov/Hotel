from django.urls import path
from apps.users.views import signup, login_user, profile
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('logout/', LogoutView.as_view(next_page= None), name='logout'),
    path('login/', login_user, name='login'),
    path('profile/<username>', profile, name='profile'),
]