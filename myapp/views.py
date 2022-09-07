import json

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from myapp.models import Education, Transport, Trytable
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from myapp.analytics.data_analysis import renderdata
from designer.dForm import LayoutForm
from designer.models import Item, ItemBloc, TypeItem, Bloc, BlocEcran, Ecran, Modele

# Create your views here.


def transport(request):
    try:
        trans = Transport.objects.all().values()
        data = renderdata(trans)
    except Transport.DoesNotExist:
        raise Http404("Transport not exist")
    return render(request, 'index.html', {'mydata': data, 'pageTitle': 'Min trans'})


def education(request):
    try:
        edu = Education.objects.all().values()
        data = renderdata(edu)
    except ObjectDoesNotExist:
        raise Http404("Object does not exist")

    return render(request, 'index.html', {'mydata': data})
