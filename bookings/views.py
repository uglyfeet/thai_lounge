from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking


@login_required
def create_booking(request):
    """Allow a customer to create a treatment booking."""

    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer = request.user
            booking.save()
            return redirect('my_bookings')
    else:
        form = BookingForm()

    return render(request, 'bookings/create_booking.html', {
        'form': form
    })


@login_required
def my_bookings(request):
    """Display bookings belonging to the logged-in customer."""

    bookings = Booking.objects.filter(
        customer=request.user
    ).order_by('booking_date', 'booking_time')

    return render(request, 'bookings/my_bookings.html', {
        'bookings': bookings
    })
