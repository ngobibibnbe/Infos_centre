from django.urls import path

from . import views
from django.views.generic import TemplateView




from django.conf.urls import  include, url
from django.contrib.auth.decorators import login_required


urlpatterns = [
     path('', views.welcome)
    ,path('vues/<id>', views.getVue)
    ,path('DeadlineIndicatorsVue/<id>', views.getDeadlineIndicatorsVue)
    ,path('DossierVue/<id>', views.getDossierVue)
    ,path('ProcedureVue/<id>', views.getProcedureVue)
    ,path('PartenaireVue/<id>', views.getPartenaireVue)





        ,path('welcome', views.welcome)

]

