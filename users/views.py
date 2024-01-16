from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import  UserSerializer
from .models import User
import jwt, datetime

class RegisterView(APIView):
    def post(self, req):
        serializer = UserSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

class LoginView(APIView):
    def post(self, req):
        username = req.data['username']
        password = req.data['password']

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found.')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password.')
        

        payload={
            'id':user.id,
            "exp": datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
            "iat":datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt':token
        }
        return  response
    
class UserView(APIView):
    def get(self, req):
        token = req.COOKIES.get("jwt")

        if not token:
            raise AuthenticationFailed('Authentication failed.')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Authentication failed.')


        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)
    

class LogoutView(APIView):
    def post(self, req):
        response = Response()
        response.delete_cookie("jwt")
        response.data={
            'message':'success'
        }
        return response