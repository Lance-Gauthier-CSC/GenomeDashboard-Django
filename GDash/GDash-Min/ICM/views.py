from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect

def ICM(request):
    context = {}
    return(request, 'ICM.html', context)