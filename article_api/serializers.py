from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import User, Group
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate, login


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])

    password = serializers.CharField(style={'input_type': 'password'}, write_only=True, required=True,
                                     validators=[validate_password])
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'email']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        group = Group.objects.get(name='follower')
        user.groups.add(group)
        user.save()

        return user


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Article
        fields = ['id', 'author', 'title', 'body', 'created', 'public']
