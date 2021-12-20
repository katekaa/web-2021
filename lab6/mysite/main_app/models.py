from django.db import models
class Lines(models.Model):
    name = models.CharField(max_length=100)
    total = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lines'