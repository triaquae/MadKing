#_*_coding:utf-8_*_
__author__ = 'jieli'
import  myauth
from rest_framework import viewsets
from serializers import UserSerializer, AssetSerializer
import models

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = myauth.UserProfile.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class AssetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Asset to be viewed or edited.
    """
    queryset = models.Asset.objects.all()
    serializer_class = AssetSerializer