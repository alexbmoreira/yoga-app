from django.core.management.base import BaseCommand, CommandError
from poses.models import Pose
from poses.poses import response


class Command(BaseCommand):
    help = "Backfill the Poses table"

    def handle(self, *args, **options):
        poses = []
        for pose in response["poses"]:
            fields = set(f.name for f in Pose._meta.get_fields())
            dct = {k: v for k, v in pose.items() if k in fields}
            try:
                poses.append(Pose(**dct))
            except Exception as e:
                print(e)


        Pose.objects.bulk_create(poses)
