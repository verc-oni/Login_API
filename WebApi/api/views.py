from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import status


# Create your views here.
class Login(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(username=email, password=password)
        
        # User Verification
        if user:      
            # Error Handling for User Token Creation
            try:
                # Response Data
                resp = {
                    "Message": f"User Successfully Created",
                    "Data": [{
                        "Token" : user.auth_token.key,
                        "email" : user.email,
                    }]
                }
                return Response(resp)
            except:
                Token.objects.create(user=user)
                resp = {
                    "Message": f"User Successfully Created",
                    "Data": [{
                        "Token" : user.auth_token.key,
                        "email" : user.email,
                    }]
                }
                return Response(resp)
        else:
            return Response({"Message": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
