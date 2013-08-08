# coding=utf-8
"""
Upload views.

Copyright (C) 2013 Nicolas Valcárcel Scerpella

Authors:
    Nicolas Valcárcel Scerpella <nvalcarcel@gmail.com>
"""
# Standard library imports
import csv
import json

# Framework imports
from django.core.files.uploadedfile import UploadedFile
from django.http import HttpResponse, HttpResponseBadRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

# 3rd party imports

# Local imports
from models import File


def show_file(request, file_id):
    f = File.objects.get(id=file_id)

    if f.file_type == 'csv':
        reader = csv.reader(f.file_obj)
        content = [x for x in reader]
    elif f.file_type == 'txt':
        content = [x for x in f.file_obj.readlines()]
    else:
        content = f.url

    data = {
        'type': f.file_type,
        'content': content
    }

    return render_to_response('details.html', data)


###########
# HELPERS #
###########


def serialize_file(file_obj):
    return {
        'id': file_obj.id,
        'name': file_obj.name,
        'type': file_obj.file_type,
        'size': file_obj.size,
        'path': file_obj.file_obj.url
    }


#######
# API #
#######


def list_files(request, page='0'):
    offset = 500 * int(page)
    start = offset
    end = 500 + offset

    files = File.objects.all()[start:end]

    ret = [serialize_file(x) for x in files]

    return HttpResponse(json.dumps(ret), mimetype='application/json')


@csrf_exempt
def upload(request):
    if request.method == 'POST':
        if not request.FILES:
            return HttpResponseBadRequest('Must have files attached!')

        file = request.FILES[u'file']
        wrapped_file = UploadedFile(file)
        filename = wrapped_file.name
        file_size = wrapped_file.file.size
        file_type = filename.split('.')[-1]

        f = File.objects.create(
            name=filename,
            file_type=file_type,
            size=file_size,
            file_obj=file
        )

    return HttpResponseRedirect('/')