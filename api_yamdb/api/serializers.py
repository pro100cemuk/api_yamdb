import datetime as dt

from rest_framework import serializers

from reviews.models import Category, Genre, Titles


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'slug')


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name', 'slug')


class TitlesSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug'
    )
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug'
    )

    class Meta:
        model = Titles
        fields = '__all__'

    def validate(self, data):
        if data['year'] > dt.datetime.now().year:
            raise serializers.ValidationError(
                'Нельзя добавлять произведения, которые еще не вышли.'
            )
        return data
