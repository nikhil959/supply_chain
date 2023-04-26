from rest_framework import viewsets
from .models import Users
from .serializers.user_serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer