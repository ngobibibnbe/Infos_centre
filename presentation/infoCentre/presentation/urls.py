from django.urls import path

from . import views
from django.views.generic import TemplateView




from django.conf.urls import  include, url
from django.contrib.auth.decorators import login_required


urlpatterns = [
     path('', login_required(TemplateView.as_view(template_name='visualisations/index.html')))
]

