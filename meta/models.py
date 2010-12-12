from django.db import models
import datetime

class Bestseller(models.Model):
    save_date = models.DateTimeField('date saved', default=datetime.datetime.now())
    sentence = models.CharField(max_length=400)
    votes = models.IntegerField(default=1)

    def __unicode__(self):
        return str(self.sentence)

