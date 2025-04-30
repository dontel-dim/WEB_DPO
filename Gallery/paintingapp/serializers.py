from rest_framework import serializers
from .forms import ExhibitionApplicationForm

class ExhibitionApplicationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone_number = serializers.CharField(max_length=15)
    artist_name = serializers.CharField(max_length=100)
    title = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    image = serializers.ImageField()
    description = serializers.CharField()
