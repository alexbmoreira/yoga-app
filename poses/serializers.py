from rest_framework import serializers

from .models import Pose


class PoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pose
        fields = (
            "base_name",
            "display_name",
            "preferred_side",
            "sideways",
            "sanskrit_name",
            "two_sided",
        )
