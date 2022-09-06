import json

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from myapp.models import Education, Transport, Trytable
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from myapp.analytics.data_analysis import renderdata
from designer.dForm import LayoutForm


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


def preview(request):
    try:
        edu = Education.objects.all().values()
        data = renderdata(edu)
        if request.method == 'POST':
            formset = LayoutForm(request.POST, request.FILES)

            if formset.is_valid:
                layout = formset.data['layout_dict']
                json_object = json.loads(layout)
                return render(request, 'preview.html', {'mydata': data, 'data_layout': json_object})
            return HttpResponseRedirect
        return HttpResponseRedirect

    except ObjectDoesNotExist:
        raise Http404("TryTab does not exist")

