from rest_framework import serializers
from user.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password']
        extra_kwargs = {
            'password' : {'write_only': True}
        }