from django.db import models

# Create your models here.
class MyDataset(models.Model):
    id = models.AutoField(primary_key=True)
    server_id = models.IntegerField(default=0)
    application_id = models.IntegerField(default=0)
    start_timestamp = models.IntegerField(default=0)
