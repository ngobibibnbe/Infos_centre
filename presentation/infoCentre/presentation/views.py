from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .models import Kibana_frame, Parent_frame
import sys
sys.setrecursionlimit(100)



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
            parent=Parent_frame.objects.get(code=code)
            frames=parent.kibanas_frame.all()
            parents=Parent_frame.objects.all()
            dico={'parents':parents}
        except Parent_frame.DoesNotExist:
            raise Http404("ce Code d'analyse n'existe pas ")
        if frames is None:
            raise Http404("y a pas d'enfants  ")
        return render(request,'visualisations/headContent/indicateur.html',{'frames':frames,'parent':parent,'user':request.user,'parents':parents})
    else:
        raise Http404("Vous n'êtes pas autorisé à rentrer ici")

def getFrameVue(request,codeParent, codeFrame):
    if request.user.is_authenticated:
        try:
            parent=Parent_frame.objects.get(code=codeParent)
            frames=parent.kibanas_frame.all()
            parents=Parent_frame.objects.all()
            dico={'parents':parents}
            frame=Kibana_frame.objects.get(code=codeFrame)
        except Parent_frame.DoesNotExist:
            raise Http404("ce Code d'analyse n'existe pas ")
        if frames is None:
            raise Http404("y a pas d'enfants  ")
        return render(request,'visualisations/headContent/indicateur.html',{'kibana_frame':frame,'frames':frames,'parent':parent,'user':request.user,'parents':parents})
        #return render(request,'visualisations/headContent/index.html',  {'kibana_frame':frame})

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
        
        return render(request,'visualisations/layout.html',{'link':link,"height":height,'user':request.user})
    else:
        raise Http404("Vous n'êtes pas autorisé à rentrer ici")

    
