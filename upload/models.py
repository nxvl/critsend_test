# coding=utf-8
"""
Upload models.

Copyright (C) 2013 Nicolas Valcárcel Scerpella

Authors:
    Nicolas Valcárcel Scerpella <nvalcarcel@gmail.com>
"""
# Standard library imports

# Framework imports
from django.db import models

# 3rd party imports

# Local imports

# Create your models here.


FILE_TYPE_CHOICES = (
    ('txt', 'Text file'),
    ('csv', 'CSV File')
)


class File(models.Model):
    name = models.CharField(max_length=20)
    file_type = models.CharField(max_length=4, choices=FILE_TYPE_CHOICES)
    size = models.IntegerField()
    file_obj = models.FileField(upload_to='files/')