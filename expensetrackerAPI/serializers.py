from rest_framework import serializers
from .models import Category, Book
from django.contrib.auth.models import User, Group

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class UserRoleSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(
        queryset = Group.objects.all(),
        slug_field = "name",
        many = True
    )

    class Meta:
        model = User 
        fields = ['id', 'username', 'groups']
    
    def update(self, instance, validated_data):
        groups = validated_data.get("groups", [])
        instance.groups.set(groups)
        instance.save()
        return instance