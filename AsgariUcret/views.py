from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.parsers import JSONParser
from AsgariUcret.models import AsgariUcret
from .serializers import UserSerializer, RegisterSerializer, LoginUserSerializer
from .serializers import AsgariUcretSerializer


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, AuthToken=None, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return JsonResponse({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

# Login Api
class AuthToken:
    objects = None

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return JsonResponse({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

# Get User Api
class UserAPI(generics.RetrieveAPIView):
    authentication_classes = (AuthTokenSerializer,)
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


@csrf_exempt
def asgariucret_api(request, id=0, asgariucret_data=None, asgariucret=None):
    if request.method == 'GET':
        asgariucret = AsgariUcret.objects.all()
        print(f"asgariucret : {asgariucret}")
        asgariucret_serializer = AsgariUcretSerializer(asgariucret, many=True)
        return JsonResponse(asgariucret_serializer.data, safe=False)
    elif request.method == 'POST':
        asgariucret_serializer = AsgariUcretSerializer(data=asgariucret_data)
        if asgariucret_serializer.is_valid():
            asgariucret_serializer.save()
            print(f"asgariucret : {asgariucret}")
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        asgariucret_data = JSONParser().parse(request)
        asgariucret = AsgariUcret.objects.get(Id=asgariucret_data['Id'])
        asgariucret_serializer = AsgariUcretSerializer(asgariucret, data=asgariucret_data)
        if asgariucret_serializer.is_valid():
            asgariucret_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        asgariucret = AsgariUcret.objects.get(Id=id)
        asgariucret.delete()
        return JsonResponse("Deleted Successfully", safe=False)


class SaveFile:
    pass
