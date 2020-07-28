from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from VDNA.models import VDNA
from django.forms import modelformset_factory
from VDNA.views import VDNA_views
from master.forms import UploadFileForm
from master.models import Session
from http import cookies
import uuid
import datetime

def index(request):
    fileUpload = UploadFileForm()

    if request.method == 'POST' and 'file' in request.FILES:
        fileUpload = UploadFileForm(request.POST, request.FILES)
        if fileUpload.is_valid():
            dbFile = request.FILES['file']
            if not request.COOKIES.get('session_id'):
                session_instance = fileUpload.save(commit=False)
                session_instance.file = dbFile
                tmp_id = uuid.uuid4()
                session_instance.session_id = str(tmp_id).replace('-', '')
                print(session_instance.session_id)
                dt = datetime.datetime.today()
                year, month = divmod(dt.month+1, 12)
                if month == 0:
                    month = 12
                    year = year - 1
                next_month = datetime.datetime(dt.year + year, month, 15)
                ses_id = session_instance.session_id
                print("Ses_id: " + ses_id)
                context = {'session_id': ses_id, 'file': str(dbFile)}
                response = render(request, 'index.html', context)
                response.set_cookie('session_id', ses_id, expires=next_month)
                session_instance.save()
            else:
                session = Session.objects.get(session_id=request.COOKIES.get('session_id'))
                session.file=dbFile
                session.save()
                context = {'session_id': request.COOKIES.get('session_id'), 
                    'file': str(dbFile)}
                response = render(request, 'index.html', context)
            return response
        else:
            return HttpResponse('Error')
    else:
        if request.COOKIES.get('session_id'):
            context = {'session_id': request.COOKIES.get(
                'session_id'), 'form': fileUpload}
        else:
            context = {'form': fileUpload}
        VDNA_views(context, request)
        response = render(request, 'index.html', context)
        return response
