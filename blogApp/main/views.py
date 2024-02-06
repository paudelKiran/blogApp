from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes
from main.models import User,Profile
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from main.serializer import UserSerializer,ProfileSerializer,LoginSerializer,categorySerializer,blogSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
import uuid
from .utils import *
from main.models import User , Profile,Categories,Blog


#!User registration view

class RegisterUser(APIView):
    def post(self,request):
        # permission_classes = (AllowAny,)
        data=request.data
        print(data)
        serializer=UserSerializer(data=data) 
        if serializer.is_valid():
            if User.objects.filter(email=serializer.data["email"]).exists():
                raise forms.ValidationError("Email already exists")
            
            else:
                #!creating the object and sending the mail to the user
                user_obj=User(email=serializer.data["email"])
                user_obj.set_password(serializer.data["password"])
                user_obj.save()

                p_obj=Profile.objects.create(
                    user=user_obj,
                    email_token=str(uuid.uuid4())
                )
                p_obj.save()
                send_email(serializer.data["email"],p_obj.email_token)
                return Response({
                    "status": True,
                    "message": "Successfully Registered. Please verify you email.",

                },status.HTTP_200_OK)
                

        return Response({
            "status": False,
            "message": serializer.errors
        },status.HTTP_400_BAD_REQUEST)


#!verifying the email after user have clicked the link sent to their mail 
class verify(APIView):
    def get(self,request,pk):
        try:
            obj=Profile.objects.get(email_token=pk)
            obj.is_verified=True
            obj.save()
            return Response("Successfully verified")
        
        except Exception as e:
            return Response("Sorry! We couldn't verify you.")

#!login api
@api_view(['POST'])
def loginUser(request):
    data=request.data
    serializer=LoginSerializer(data=data)

    if not serializer.is_valid(): #serializer sanga validate gareko
        return Response({
            "status": False,
            "message": serializer.errors
        },status.HTTP_400_BAD_REQUEST)

    user=authenticate(email=serializer.data["email"], password=serializer.data["password"]) #direct authenication 
    if not user: #if user not available
         return Response({
            "status": False,
            "message": "Invalid credentials."
        },status.HTTP_400_BAD_REQUEST)
    else:
        if Profile.objects.get(user=user).is_verified==True:
            token = Token.objects.get_or_create(user=user)
            return Response({
                "status": True,
                "message": "Enjoy dear..👍",
                "token":str(token),
            },status.HTTP_200_OK)

        else:
            return Response({
                "status": False,
                "message": "Please verify your email first."
            },status.HTTP_400_BAD_REQUEST)


#!category CRUD operation
class getCategory(generics.ListAPIView):
    queryset=Categories.objects.all()
    serializer_class=categorySerializer

class createCategory(generics.CreateAPIView):
    serializer_class=categorySerializer
    

#!blog CRUD operations 
class getBlog(generics.ListAPIView):
    queryset=Blog.objects.all()
    serializer_class=blogSerializer

class createBlog(generics.CreateAPIView):
    serializer_class=blogSerializer

class updateBlog(generics.UpdateAPIView):
    serializer_class=blogSerializer



