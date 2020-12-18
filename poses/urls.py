from django.urls import path

from .views import PoseListAPIView, PoseDetailAPIView

urlpatterns = [
    path('', PoseListAPIView.as_view()),
    path('<int:pose_id>', PoseDetailAPIView.as_view()),
]
