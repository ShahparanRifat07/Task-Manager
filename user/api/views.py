from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password


from .serializers import UserRegistrationSerializer
from user.models import User


class UserRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data
        password = validated_data.get('password')
        hashed_password = make_password(password) 
        validated_data['password'] = hashed_password

        user = serializer.save()
        
        refresh = RefreshToken.for_user(user)
        response_data = {
            'username': user.username,
            'email': user.email,
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        }
        

        return Response(response_data, status=status.HTTP_201_CREATED)
