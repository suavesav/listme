from rest_framework import serializers
from listme.models import List, ListElement
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    lists = serializers.PrimaryKeyRelatedField(many=True, queryset=List.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'lists')

class ListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model=List
        fields = ('name', 'owner', 'show_list', 'is_public')

class ListElementSerializer(serializers.ModelSerializer):
    class Meta:
        model=ListElement
        fields = ('text', 'show_element', 'completed')
