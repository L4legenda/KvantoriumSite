from django.db import models

# Create your models here.

class Teachers(models.Model):
	name = models.CharField(max_length=40)
	surname = models.CharField(max_length=40)
	patronymic = models.CharField(max_length=40)
	kvantum = models.CharField(max_length=30)

