from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^memos/$', views.memo_list),
    url(r'^persons/$', views.person_list),
    url(r'^newmemo/$', views.new_memo),
    url(r'^memopersons/$', views.memo_person_list),
]