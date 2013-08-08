# coding=utf-8
"""
Copyright (C) 2013 Nicolas Valcárcel Scerpella

Authors:
    Nicolas Valcárcel Scerpella <nvalcarcel@gmail.com>
"""
# Standard library imports

# Framework imports
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

# 3rd party imports

# Local imports


urlpatterns = patterns(
    '',
    url(r'^$',
        TemplateView.as_view(template_name='home.html')),
    url(r'^(?P<file_id>\d+)/$',
        'upload.views.show_file',
        name='file_detail'),

    url(r'^api/list$',
        'upload.views.list_files',
        name='list'),
    url(r'^api/list/(?P<page>\d+)$',
        'upload.views.list_files',
        name='list'),
    url(r'^api/upload/$',
        'upload.views.upload',
        name='upload'),
)
