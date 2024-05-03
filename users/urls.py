from django.urls import path
from users.views.login import login_user
from users.views.sign_up import sign_up
from users.views.logout import logout_user

urlpatterns = [
    path('', login_user, name='login'),
    path('sign-up/', sign_up, name='sign_up'),
    path('logout/', logout_user, name='logout')
]