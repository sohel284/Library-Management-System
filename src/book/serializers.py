from rest_framework import serializers

from book.models import Book, Author, CopyOfBook

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class CopyOfBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = CopyOfBook
        fields = '__all__'







