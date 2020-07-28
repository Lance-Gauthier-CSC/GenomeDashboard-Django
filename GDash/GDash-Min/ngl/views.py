from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage()
def ngl(request):
    print(fs.listdir('../GDash-Min/tmp')[1])
    # files = fs.listdir('../gdash/tmp')[1]
    # if len(files) > 0:
    #     print('files found')
    #     file = files[len(files)-1]
    #     data = fs.open(file)
    #     print(fs.open(file).read())
    #     print(file)
    #     context = {'file': data}
    #     return render(request, 'jsmol/index.html', context)
    return render(request, 'ngl.html')