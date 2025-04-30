from rest_framework import serializer
from .models import CustomUser

class UserSerializer(serializer.ModelSerializer):
    password = serializer.charField(write_only=True, min_length=8)
    
    class Meta:
        Models = CustomUser
        fields = ['id', 'username', 'email', 'password', 'documento', 'telefono']
        
    def create(self, validated_data):
        return CustomUser.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['pasword'],
            documento = validated_data.get['documento', ''],
            telefono = validated_data.get['telefono', '']
        )