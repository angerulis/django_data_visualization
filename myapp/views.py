import json

from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from myapp.models import Education, Transport
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from myapp.analytics.data_analysis import renderdata, renderdata1
from designer.dForm import LayoutForm
from designer.models import Item, ItemBloc, TypeItem, Bloc, BlocEcran, Ecran, Modele, Utilisateur
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth import authenticate, login, logout, models


# Create your views here.

# get layout from ecran id and return layout dictionary
def get_layout(current_ecran_id, as_json=False):
    if not isinstance(current_ecran_id, int):
        return {}
    layout = dict()
    bloc_ecran = BlocEcran.objects.filter(ecran_id=current_ecran_id).order_by('y')
    i = 1
    for be in bloc_ecran.values():  # iterate through all BlocEcran instances
        bloc = {}
        j = 1
        for bl in ItemBloc.objects.values('item_id', 'x').filter(bloc_id=be['bloc_id']).order_by('x'):
            # iterate each bloc
            # bloc_id = be['bloc_id']
            # item_bloc = ItemBloc.objects.order_by('x').values('item_id', 'x').get(bloc_id=bloc_id)
            # get item model instance label from bloc id
            item = Item.objects.values('item_libelle').get(item_id=bl.get('item_id'))
            bloc['card' + str(j)] = item['item_libelle']
            j += 1

        layout[i] = bloc
        i = i + 1

        if as_json:
            return json.dumps(layout)
    return layout


def login_request(request):
    user = request.user
    if user.is_authenticated and not user.is_anonymous:
        return redirect('transport')

    error_message = False
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                user_profile = Utilisateur.objects.filter(utilisateur=request.user.id).values().get()
                request.session['username'] = request.user.get_username()
                request.session['fname'] = user_profile["utilisateur_prenom"]
                request.session['lname'] = user_profile['utilisateur_nom']
                request.session['email'] = user_profile['utilisateur_email']
                request.session['contact'] = user_profile['utilisateur_contact']
                request.session['fonction'] = user_profile['utilisateur_fonction']
                request.session.set_expiry(600)
                # messages.info(request, f"You are now logged in as {username}")
                return redirect('transport')

            error_message = True
        error_message = True
    form = AuthenticationForm()
    return render(request=request, template_name="login.html",
                  context={"form": form, 'ERROR_MESSAGE': error_message})


@login_required
def logout_request(request):
    logout(request)
    return redirect('transport')


@login_required
@permission_required('myapp.view_transport', raise_exception=True)
def transport(request):
    try:
        trans = Transport.objects.all().values()
        data = renderdata1(trans)
        jsonlayout = json.dumps(get_layout(38))

    except ObjectDoesNotExist:
        raise Http404("Object does not exist")

    return render(request, 'index.html', {
        'mydata': data, 'mylayout': jsonlayout, 'session': request.session,
        'page_title': 'Ministère du transport', 'user': request.user})


@login_required
@permission_required('myapp.view_education')
def education(request):
    try:
        rubrique = []
        edu = Education.objects.all().values()
        data = renderdata(edu)
        jsonlayout = json.dumps(get_layout(38))


    except ObjectDoesNotExist:
        raise Http404("Object does not exist")

    user = request.user
    return render(request, 'index.html', {'mydata': data, 'mylayout': jsonlayout,
                                          'page_title': "Ministère de l'education Nationale ",
                                          })
