from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Pose
from .serializers import PoseSerializer


class PoseListAPIView(ListAPIView):
    queryset = Pose.objects.all()
    serializer_class = PoseSerializer
    permission_classes = ()


class PoseDetailAPIView(RetrieveAPIView):
    queryset = Pose.objects.all()
    serializer_class = PoseSerializer
    permission_classes = ()
    lookup_url_kwarg = 'pose_id'
