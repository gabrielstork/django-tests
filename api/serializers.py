from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from accounts.models import Account
from posts.models import Post, Comment


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(
        write_only=True, style={'input_type': 'password'},
    )

    class Meta:
        model = Account

        fields = (
            'id',
            'username',
            'email',
            'password',
            'followers',
            'following',
            'account_posts',
            'account_comments',
            'liked_posts',
            'is_active',
            'is_staff',
            'url',
        )

        read_only_fields = (
            'followers',
            'following',
            'account_posts',
            'account_comments',
            'is_active',
        )

    def create(self, validated_data):
        validated_data['password'] = make_password(
            validated_data.get('password')
        )

        if validated_data.get('is_staff'):
            validated_data['is_superuser'] = True

        return super().create(validated_data)


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post

        fields = (
            'id',
            'author',
            'title',
            'text',
            'comments',
            'likes',
            'url',
        )


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment

        fields = (
            'id',
            'author',
            'post',
            'text',
            'url',
        )
