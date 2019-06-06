from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'snippets/$',views.snippet_list),
    url(r'snippets/(?P<pk>[\w-]+)/$', views.snippet_detail)
]