from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .models import Kibana_frame, Parent_frame




template_name=""

def welcome(request):
    if request.user.is_authenticated:
        parents=Parent_frame.objects.all()
        dico={'parents':parents}
        return render(request,'visualisations/welcome.html',dico)
    else:
        raise Http404("Vous n'êtes pas autorisé à rentrer ici")



def getParentVue(request,code):
    if request.user.is_authenticated:
        try:
            frames=Parent_frame.objects.get(code=code).kibanas_frame.all()
        except Parent_frame.DoesNotExist:
            raise Http404("ce Code d'analyse n'existe pas ")
        
        return render(request,'visualisations/headContent/indicateur.html',{"height":frames,'user':request.user})
    else:
        raise Http404("Vous n'êtes pas autorisé à rentrer ici")



def getDeadlineIndicatorsVue(request,id):
    if request.user.is_authenticated:
        try:
            link=Kibana_frame.objects.get(code=id).link
            height=Kibana_frame.objects.get(code=id).height
        except Kibana_frame.DoesNotExist:
            raise Http404("ce Code d'analyse n'existe pas ")
        
        return render(request,'visualisations/headContent/indicateur.html',{'link':link,"height":height,'user':request.user})
    else:
        raise Http404("Vous n'êtes pas autorisé à rentrer ici")


def getDossierVue(request,id):
    if request.user.is_authenticated:
        try:
            link=Kibana_frame.objects.get(code=id).link
            height=Kibana_frame.objects.get(code=id).height
        except Kibana_frame.DoesNotExist:
            raise Http404("ce Code d'analyse n'existe pas ")
        
        return render(request,'visualisations/headContent/dossier.html',{'link':link,"height":height,'user':request.user})
    else:
        raise Http404("Vous n'êtes pas autorisé à rentrer ici")



def getProcedureVue(request,id):
    if request.user.is_authenticated:
        try:
            link=Kibana_frame.objects.get(code=id).link
            height=Kibana_frame.objects.get(code=id).height
        except Kibana_frame.DoesNotExist:
            raise Http404("ce Code d'analyse n'existe pas ")
        
        return render(request,'visualisations/headContent/procedure.html',{'link':link,"height":height,'user':request.user})
    else:
        raise Http404("Vous n'êtes pas autorisé à rentrer ici")

def getPartenaireVue(request,id):
    if request.user.is_authenticated:
        try:
            link=Kibana_frame.objects.get(code=id).link
            height=Kibana_frame.objects.get(code=id).height
        except Kibana_frame.DoesNotExist:
            raise Http404("ce Code d'analyse n'existe pas ")
        
        return render(request,'visualisations/headContent/partenaire.html',{'link':link,"height":height,'user':request.user})
    else:
        raise Http404("Vous n'êtes pas autorisé à rentrer ici")


def getVue(request,id):
    if request.user.is_authenticated:
        try:
            link=Kibana_frame.objects.get(code=id).link
            height=Kibana_frame.objects.get(code=id).height
        except Kibana_frame.DoesNotExist:
            raise Http404("ce Code d'analyse n'existe pas ")
        
        return render(request,'visualisations/index.html',{'link':link,"height":height,'user':request.user})
    else:
        raise Http404("Vous n'êtes pas autorisé à rentrer ici")

    
