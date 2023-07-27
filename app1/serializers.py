from rest_framework import serializers
from .models import premium,prem,pair,products

class premiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = premium
        fields = ['card', 'cvv', 'email', 'password']

class premSerializer(serializers.ModelSerializer):
    class Meta:
        model = prem
        fields = ['ard', 'vv', 'mail', 'assword']


class pairSerializer(serializers.ModelSerializer):
    class Meta:
        model = pair
        fields = ['rd', 'v', 'ail', 'ssword']

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = '__all__'