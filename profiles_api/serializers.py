from rest_framework import serializers
from profiles_api import models # This is my written python code


# For testing purposes
class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)


# We're using Model.Serializer as it provides way more functionalities
class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

# To set extra features to password field
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user
