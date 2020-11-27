from django.conf.urls import url, include

from accounts import urls as accounts_urls
from lists import views

urlpatterns = [
    url(r'^new$', views.new_list, name='new_list'),
    url(r'^(\d+)/$', views.view_list, name='view_list'),
    url(r'^accounts/', include(accounts_urls)),
]
