from django.db import models
from django.contrib.auth.models import User
from treatments.models import Treatment


class Booking(models.Model):
    """Model representing a customer treatment booking."""

    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bookings'
    )
    treatment = models.ForeignKey(
        Treatment,
        on_delete=models.CASCADE
    )
    booking_date = models.DateField()
    booking_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.username} - {self.treatment.name}"
