from django.db import models

class Record(models.Model):
    heart_beat        = models.IntegerField()
    blood_pressure    = models.IntegerField()
    body_temperature  = models.DecimalField(max_digits=3, decimal_places=1)
    oxygen_saturation = models.IntegerField()
    created_at        = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table = "records"