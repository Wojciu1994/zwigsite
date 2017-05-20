# -*- coding: utf-8 -*-
from django.conf.urls import url
from myapp.views import list
from myapp.views import detail, model

urlpatterns = [
    url(r'^list/$', list, name='list'),
    url(r'^(?P<document_id>[0-9]+)/$', detail, name='detail'),
    url(r'^model/$', model, name='model'),
]