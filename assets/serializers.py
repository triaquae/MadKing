#_*_coding:utf-8_*_
__author__ = 'jieli'
from myauth import UserProfile
import models
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('url', 'name', 'email')


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Asset
        fields = ('name', 'sn','server')


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Server
        #fields = ('name', 'sn','server')