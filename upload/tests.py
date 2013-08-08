# coding=utf-8
"""
Upload tests.

Copyright (C) 2013 Nicolas Valcárcel Scerpella

Authors:
    Nicolas Valcárcel Scerpella <nvalcarcel@gmail.com>
"""
# Standard library imports
import json

# Framework imports
from django.test.client import Client

# 3rd party imports
import pytest

# Local imports
from upload.models import File as My_File
from upload.views import serialize_file


def create_files():
    file_types = ('txt', 'csv')
    for x in range(10):
        file_type = file_types[x % 2]

        f = My_File.objects.create(
            name='test file %d' % x,
            file_type=file_type,
            size=x * 100,
            file_obj='test/file/path.txt'
        )
        f.save()


@pytest.mark.django_db
def test_file_model():
    create_files()

    assert My_File.objects.count() == 10


def test_add():
    c = Client()
    response = c.get('/add')

    assert response.status_code == 200
    assert response.templates[0].name == 'add.html'


def test_home():
    c = Client()
    response = c.get('/')

    assert response.status_code == 200
    assert response.templates[0].name == 'home.html'


def test_serialize_file():
    class Mock(object):
        class FileObj(object):
            url = 'test/path'

        name = 'test name'
        file_type = 'test type'
        size = 100500
        file_obj = FileObj()

        def __init__(self):
            self.id = 1

    assert serialize_file(Mock()) == {
        'id': 1,
        'name': 'test name',
        'type': 'test type',
        'size': 100500,
        'path': 'test/path'
    }

@pytest.mark.django_db
def test_api_list_files():
    create_files()
    file_types = ('txt', 'csv')

    c = Client()
    response = c.get('/api/list')
    res = json.loads(response.content)

    assert res == [
        {
            u'id': x + 1,
            u'name': u'test file %d' % x,
            u'type': file_types[x % 2],
            u'size': x * 100,
            u'path': u'test/file/path.txt'
        } for x in range(10)
    ]

    response = c.get('/api/list/2')
    res = json.loads(response.content)

    assert res == []