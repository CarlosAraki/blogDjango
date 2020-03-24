from django.db import models

class test_model(models.Model):
    name = models.CharField(max_length = 50)
    exclude = models.CharField(max_length = 3)
