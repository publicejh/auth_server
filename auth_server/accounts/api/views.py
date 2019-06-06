from rest_framework import generics
from rest_framework_api_key.permissions import HasAPIKey
from .serializers import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = []
    permission_classes = (HasAPIKey, )
    queryset = User.objects.all()
    serializer_class = UserSerializer
