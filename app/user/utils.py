from .serializers import UserRegistrationSerializer, UserLoginSerializer
from rest_framework.response import Response
from rest_framework import status

def send_login_request(request, Default=None):
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    response = {
        'success': 'True',
        'status code': status.HTTP_200_OK,
        'message': 'User logged in  successfully',
        'token': serializer.data['token'],
    }
    status_code = status.HTTP_200_OK

    return Response(response, status=status_code)

def send_registration_request(request, Default = None):
    serializer = UserRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    status_code = status.HTTP_201_CREATED
    response = {
        'success': 'True',
        'status code': status_code,
        'message': 'User registered  successfully',
    }

    return Response(response, status=status_code)