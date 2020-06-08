from django.urls import path

from . import views
from django.views.generic import TemplateView




from django.conf.urls import  include, url
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^logout/$', views.LogoutView.as_view()),
    url(r'^visualise/$', login_required(TemplateView.as_view(template_name='backoffice/index.html'))),
    path('', login_required(TemplateView.as_view(template_name='visualisations/index.html')))
]

