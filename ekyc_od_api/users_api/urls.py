from django.urls import path
from users_api.views import UserCreateView, UserDetailView

urlpatterns = [
    # path('', UserCreateView.as_view(), name='user-create'),
    # path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('me/', UserDetailView.as_view(), name='user-detail'),
]
