from django.db import models

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def fancy_name(self):
        return self.name + "!!!"