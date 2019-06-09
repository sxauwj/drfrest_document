from django.conf.urls import url, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'snippets/$', views.SnippetListView.as_view()),
    url(r'snippets/(?P<pk>[\w]+)/$', views.SnippetDetailView.as_view()),
    url(r'user', views.UserList.as_view()),
    url('user/(?P<pk>[\w])/$', views.UserDetail.as_view())


]
urlpatterns = format_suffix_patterns(urlpatterns)
