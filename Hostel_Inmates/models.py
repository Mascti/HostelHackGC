from __future__ import unicode_literals

from django.db import models

class Inmate(models.Model):
    Name = models.CharField(max_length=200)
    Room_Number = models.IntegerField(primary_key=True)
    Mobile = models.IntegerField()

    def __str__(self):
        return self.Room_Number + ' - ' +self.Name
