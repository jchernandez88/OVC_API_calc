#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from rest_framework import serializers
from models import Operacion

class OperacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Operacion
        fields = ('url', 'op1', 'op2', 'operacion', 'resultado')
