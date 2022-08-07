from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse

from .models import HealthCenter
from .serializer import HealthCentersSirializer


def health_centers_list(request):
    health_centers = HealthCenter.objects.all()
    serializer = HealthCentersSirializer(health_centers, many=True)
    return JsonResponse(serializer.data, safe=False)
