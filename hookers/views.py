from django.shortcuts import render
from rest_framework.generics import *
from .serializers import HookersModelSerializer
from .models import Hooker
# Create your views here.


class HookersListView(ListCreateAPIView):
    permission_classes = ()
    serializer_class = HookersModelSerializer
    model = Hooker
    queryset = Hooker.objects.all()
