from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from child_health.filters import PregnancyFilter
from child_health.models import Child, Pregnancy, Vaccine
from child_health.serializers import ChildSerializer, PregnancySerializer, VaccineSerializer


class PregnancyViewSet(ModelViewSet):
    queryset = Pregnancy.objects.all()
    serializer_class = PregnancySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = PregnancyFilter

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    @action(detail=False, methods=['get'])
    def active(self, request):
        active_pregnancy = Pregnancy.objects.get_active_pregnancy_for_user(request.user)
        if active_pregnancy is not None:
            serializer = self.get_serializer(active_pregnancy, many=False)
            return Response(serializer.data)
        return Response(status=404)


class ChildrenViewSet(ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class VaccinesViewSet(ListModelMixin, GenericViewSet):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(is_active=True)
