from django.db import models


class Pose(models.Model):

    NA = "NA"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    preferred_side_options = [
        (NA, "Not available"),
        (LEFT, "Left"),
        (RIGHT, "Right"),
    ]
    base_name = models.CharField(max_length=100, blank=False, unique=True)
    display_name = models.CharField(max_length=100, blank=False)
    preferred_side = models.CharField(
        max_length=10, choices=preferred_side_options, default=NA
    )
    sideways = models.BooleanField(default=False)
    sanskrit_name = models.CharField(max_length=100, null=True)
    two_sided = models.BooleanField(default=False)
