from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'id',
        ]


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'id',
            'email',
        ]


class UserOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
