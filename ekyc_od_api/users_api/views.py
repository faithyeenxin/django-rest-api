from django.contrib.auth.models import User
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import UserSerializer
from .custom_permissions import IsSuperUser
from rest_framework.generics import ListCreateAPIView

# ONLY CAN POST, CANNOT VIEW ALL USERS
# class UserCreateView(CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsSuperUser,)  

# CAN VIEW, CAN POST
class UserCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,) 


class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
