from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect

def dalliance(request):
    return render(request, 'dalliance.html')