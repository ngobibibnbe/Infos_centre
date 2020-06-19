from django.shortcuts import render
from django.contrib.auth.models import User , Group
from rest_framework import viewsets
# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from .serializer import UserSerializer,GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = GroupSerializer


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def UpdateUser(request):
    payload = json.loads(request.body,user_id)

    try:
        user = User.objects.filter( id=user_id)
        # returns 1 or 0
        user.update(**payload)
        user = user.objects.get(id=user_id)
        serializer = UserSerializer(user)
        return JsonResponse({'user': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.views.generic import TemplateView
from django.conf import settings

def page_not_found_view(request,Exception):
     return render(request,'errors/404.html')
        
    
class LoginView(TemplateView):

  template_name = 'login/login.html'

  def post(self, request, **kwargs):

    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        return HttpResponseRedirect( settings.LOGIN_REDIRECT_URL )

    return render(request, self.template_name,{'user':request.user})


class LogoutView(TemplateView):

  template_name = 'login/login.html'

  def get(self, request, **kwargs):

    logout(request)

    return render(request, self.template_name)