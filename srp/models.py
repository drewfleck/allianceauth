from django.db import models

from eveonline.models import EveCharacter


class SrpFleetMain(models.Model):
    fleet_name = models.CharField(max_length=254, default="")
    fleet_doctrine = models.CharField(max_length=254, default="")
    fleet_time = models.DateTimeField()
    fleet_srp_code = models.CharField(max_length=254, default="", unique=True)
    fleet_srp_status = models.CharField(max_length=254, default="")
    fleet_commander = models.ForeignKey(EveCharacter)
    fleet_srp_aar_link = models.CharField(max_length=254, default="")

    def __str__(self):
        return self.fleet_name + " - SrpFleetMain"


class SrpUserRequest(models.Model):
    killboard_link = models.CharField(max_length=254, default="")
    after_action_report_link = models.CharField(max_length=254, default="")
    additional_info = models.CharField(max_length=254, default="")
    srp_status = models.CharField(max_length=254, default="")
    srp_total_amount = models.BigIntegerField(default=0)
    character = models.ForeignKey(EveCharacter)
    srp_fleet_main = models.ForeignKey(SrpFleetMain)

    def __str__(self):
        return self.character.character_name + " - SrpUserRequest"