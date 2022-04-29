from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
def test(request):
    # myuser= User.objects.create_user(first_name = "vinay", password = "poylpl2qg" ,username="vinay")
    # myuser.save()
    print("testing")
    # print(request.data)
    # return JsonResponse({'success':'true'})
    return HttpResponse("hello")

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])






class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def SignUp(request):
    myuser= User.objects.create_user(first_name = request.data["name"], password = request.data["password"] ,username=request.data["username"])
    myuser.save()
    return JsonResponse({"respone" : f"New User Created with usrname {myuser.username} "})


@api_view(['POST'])
def usernameavailibility(request):
    print(request.data["username"])
    try:
        user = User.objects.get(username=request.data["username"])
        return JsonResponse({'available':'false'})
    except:
        return JsonResponse({'available':'true'})
    # return JsonResponse({"result":"connected"})
