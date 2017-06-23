from django.conf.urls import include, url
from assets import views

urlpatterns = [
    url(r'report/$', views.asset_report, name='asset_report'),
    # url(r'report/bulk_create/$',views.bulk_create_assets,name='bulk_create_assets' ),
    url(r'report/asset_with_no_asset_id/$', views.asset_with_no_asset_id, name='acquire_asset_id'),
    url(r'^report_test/$', views.asset_report_test),
    url(r'^acquire_asset_id_test/$', views.acquire_asset_id_test),
    url(r'^new_assets/approval/$', views.new_assets_approval, name="new_assets_approval"),
    url(r'^asset_list/$', views.asset_list, name="asset_list"),
    url(r'^asset_list/(\d+)/$', views.asset_detail, name="asset_detail"),
    url(r'^asset_list/list/$', views.get_asset_list, name="get_asset_list"),
    url(r'^asset_list/category/$', views.asset_category, name="asset_category"),
    url(r'^asset_event_logs/(\d+)/$', views.asset_event_logs, name="asset_event_logs"),
    url(r'^event_center/$',views.event_center,name="event_center")

]
