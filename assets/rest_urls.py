#_*_coding:utf-8_*_
__author__ = 'jieli'
from django.conf.urls import url, include
from rest_framework import routers
from assets import rest_views as views
from assets import views as asset_views
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'assets', views.AssetViewSet)
router.register(r'servers', views.ServerViewSet)


from assets import rest_test
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'asset_list/$',views.AssetList ),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^dashboard_data/',asset_views.get_dashboard_data,name="get_dashboard_data"),
    url(r'^eventlogs/$', rest_test.eventlog_list),
]