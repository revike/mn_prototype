from django.contrib.auth.models import User
from rest_framework import serializers

from main.models import Board, BoardData


class AuthorModelSerializer(serializers.ModelSerializer):
    """Сериализатор автора"""

    class Meta:
        model = User
        fields = ['id', 'username', 'last_name', 'first_name', 'email']


class BoardModelSerializer(serializers.ModelSerializer):
    """Сериализатор для доски"""

    author = AuthorModelSerializer(read_only=True)

    class Meta:
        model = Board
        fields = ['id', 'author', 'group', 'name', 'description']


class BoardDataModelSerializer(serializers.ModelSerializer):
    """Сериализатор данных доски"""

    board = BoardModelSerializer(read_only=True)

    class Meta:
        model = BoardData
        fields = '__all__'
