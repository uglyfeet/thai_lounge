from django.db import models


class Treatment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
