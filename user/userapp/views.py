from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from userapp.serializers import RegisterSerializer, LogInSerializer, LogOutSerializer, UpdateSerializer, DeleteSerializer, ChangePasswordSerializer
from rest_framework import response, status, generics, permissions
from django.contrib.auth import authenticate, logout
from rest_framework.views import APIView
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core.mail import send_mail

# Create your views here.


class RegisterAPIView(GenericAPIView):

    serializer_class = RegisterSerializer

   
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                email = request.data.get('email')
                send_mail(
                subject='Registration Verification',
                message= 'Hello, You Are Registered Successfully',
                from_email= 'roshan.chavhan@thinkitive.com',
                recipient_list= [email],
                fail_silently=False,
                )
            
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogInAPIView(GenericAPIView):
    serializer_class = LogInSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            serializer = self.serializer_class(user)

            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response({'Inavlid Crendential ,Try Again'}, status=status.HTTP_401_UNAUTHORIZED)


class LogOutAPIView(GenericAPIView):
    serializer_class = LogOutSerializer

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = authenticate(email=email, password=password)

        if user:
            logout(request)

            return response.Response({'message': "Logout successful"})
        return response.Response({'message': "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class DeleteAPIView(GenericAPIView):
    def delete(self, request, pk, **kwargs):
        user = CustomUser.objects.get(id=pk)
        user.delete()
        return response.Response({"result": "user deleted"})


class UpdateAPIView(GenericAPIView):
    user = CustomUser.objects.all()
    serializer_class = UpdateSerializer

    def get(self, request, pk):
        try:
            obj = CustomUser.objects.get(id=pk)
        except CustomUser.DoesNotExist:
            msg = {"message": "User Not Found"}
            return response. Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = UpdateSerializer(obj)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            obj = CustomUser.objects.get(id=pk)
        except (UpdateSerializer.DoesNotExist, AttributeError):
            msg = {"message": "User Not Found Error"}
            return response.Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = UpdateSerializer(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response({"msg": "User Updated"}, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(UpdateAPIView):

    serializer_class = ChangePasswordSerializer
    model = CustomUser

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password

            if not self.object.check_password(serializer.data.get("old_password")):
                return response.Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response1 = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return response.Response(response1)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HelloView(GenericAPIView):
    permission_classes = (IsAuthenticated)

    def get(self, request):
        content = {'message': 'Hello'}
        return response.Response(content)
