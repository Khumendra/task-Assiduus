from django.shortcuts import render
from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer, GetMessageSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response



# Create your views here.
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    http_method_names = ['get', 'post', 'retrieve']

    def get_queryset(self):
        return Message.objects.filter(created_by=self.request.user.pk).all()


class GetMessageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Message.objects.all()
    serializer_class = GetMessageSerializer




# ===================Custom Token Login ======================
class CustomAuthTokenLogin(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })
