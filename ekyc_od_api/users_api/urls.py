from django.urls import path
from users_api.views import UserCreateView, UserDetailView, LoginView

urlpatterns = [
    path('create/', UserCreateView.as_view(), name='user-create'),
    path('me/', UserDetailView.as_view(), name='user-detail'),
    path('auth/login/', LoginView.as_view(), name='login'),
]
