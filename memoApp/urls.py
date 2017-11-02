from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^memos/$', views.memo_list),
    url(r'^persons/$', views.person_list),
]