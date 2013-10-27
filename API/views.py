#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from rest_framework import viewsets
from API.serializers import OperacionSerializer
from models import Operacion

class OperacionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Operacion.objects.all()
    serializer_class = OperacionSerializer


