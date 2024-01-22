from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'password', 'username']
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            user = User(
                username=validated_data['username'],
            )
            user.set_password(validated_data['password'])
            user.save()
            return user


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']

        def create(self, validated_data):
            return self.Meta.model.objects.create_user(**validated_data)


class UserLogoutSerializer(serializers.Serializer):
    login = serializers.CharField()
    password = serializers.CharField(min_length=8, max_length=32)
