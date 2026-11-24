from datetime import datetime

from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """Form for creating and editing customer bookings."""

    TIME_CHOICES = [
        (f'{hour:02d}:{minute:02d}', f'{hour:02d}:{minute:02d}')
        for hour in range(10, 20)
        for minute in (0, 30)
    ]

    booking_time = forms.TypedChoiceField(
        choices=TIME_CHOICES,
        label='Appointment Time',
        coerce=lambda value: datetime.strptime(
            value, '%H:%M'
        ).time()
    )

    class Meta:
        model = Booking
        fields = ['treatment', 'booking_date', 'booking_time']

        widgets = {
            'booking_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }
