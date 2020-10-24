from django.shortcuts import render
from rest_framework import viewsets

from .models import (ClientInfo, ClientPersDoc, ClientState, PlatformRule,
                     Qualification)
from .serializers import (ClientInfoSerializer, ClientPersDocSerializer,
                          ClientStateSerializer, PlatformRuleSerializer,
                          QualificationSerializer)


class ClientInfoViewSet(viewsets.ModelViewSet):
    queryset = ClientInfo.objects.all()
    serializer_class = ClientInfoSerializer


class ClientPersDocViewSet(viewsets.ModelViewSet):
    queryset = ClientPersDoc.objects.all()
    serializer_class = ClientPersDocSerializer
    lookup_field = 'client'


class ClientStateViewSet(viewsets.ModelViewSet):
    queryset = ClientState.objects.all()
    serializer_class = ClientStateSerializer
    lookup_field = 'client'


class PlatformRuleViewSet(viewsets.ModelViewSet):
    queryset = PlatformRule.objects.all()
    serializer_class = PlatformRuleSerializer
    lookup_field = 'client'


class QualificationViewSet(viewsets.ModelViewSet):
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer
    lookup_field = 'client'
