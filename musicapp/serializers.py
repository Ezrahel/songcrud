from rest_framework import serializers
from rest_framework import routers, serializers, viewsets
from musicapp.models import Artist, Song, Lyric

class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name = 'details',
        lookup_field = 'pk')
    class Meta:
        model = Artist
        fields = [
            'first_name',
            'last_name',
            'age',
            'url',
            ]

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Artist.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance


class SongSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name = 'details',
        lookup_field = 'pk')
    class Meta:
        model = Song
        fields = [
            'title',
            'date_released',
            'likes',
            'artist_id',
            'url',
            ]

    
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Song.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.date_released = validated_data.get('date_released', instance.date_released)
        instance.likes = validated_data.get('likes', instance.likes)
        instance.artist_id = validated_data.get('artist_id', instance.artist_id)
        instance.save()
        return instance


class LyricSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name = 'details',
        lookup_field = 'pk')
    class Meta:
        model = Lyric
        fields = [
            'content',
            'song_id',
            'url',
            ]

    
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Lyric.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.content = validated_data.get('content', instance.content)
        instance.song_id = validated_data.get('song_id', instance.song_id)
        instance.save()
        return instance