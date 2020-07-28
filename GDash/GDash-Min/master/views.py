from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from VDNA.models import VDNA
from django.forms import modelformset_factory
from VDNA.views import VDNA_views

def index(request):
    context = {}
    VDNA_views(context, request)
    return render(request, 'index.html', context)
