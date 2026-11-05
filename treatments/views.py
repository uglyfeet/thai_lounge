from django.shortcuts import render
from .models import Treatment


def treatment_list(request):
    treatments = Treatment.objects.filter(active=True)

    context = {
        'treatments': treatments,
    }

    return render(
        request,
        'treatments/treatment_list.html',
        context,
    )
