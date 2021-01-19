from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from .utils import send_login_request, send_registration_request

class UserRegistrationView(CreateAPIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        return send_registration_request(request)

class UserLoginView(RetrieveAPIView):

    permission_classes = (AllowAny,)

    def post(self, request):
        return send_login_request(request)
