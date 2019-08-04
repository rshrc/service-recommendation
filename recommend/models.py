from django.contrib.auth.models import AbstractUser
from django.db import models


# class TargetCustomer(AbstractUser):
#     pass


class RecommendModel(models.Model):
    """
    Maybe need to add more parameters
    """
    user_id = models.IntegerField()
    residing_city = models.CharField(max_length=10)
    residing_country = models.CharField(max_length=10)
    total_purchase = models.DecimalField(max_digits=5, decimal_places=2)
    total_cost = models.DecimalField(max_digits=5, decimal_places=2)
