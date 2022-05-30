from rest_framework import serializers
from .models import Subjects, Photo


class SubjectsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subjects
        fields = '__all__'


class Title_nested_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subjects
        fields = ['url', 'title']


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    related_title = Title_nested_Serializer()

    class Meta:
        model = Photo
        fields = ['url', 'image', 'related_title']
