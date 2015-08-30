
from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'report/$',views.asset_report,name='asset_report' ),
    url(r'^report_test/$',views.asset_report_test ),


]
