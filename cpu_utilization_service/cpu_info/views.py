from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import CpuInfoSlice
from .serializers import CpuInfoSliceSerializer


class CpuInfoSliceViewSet(ModelViewSet):
    serializer_class = CpuInfoSliceSerializer
    queryset = CpuInfoSlice.objects.order_by("-created_at")[:100]

    @action(detail=False, methods=["GET"])
    def last_records_average(self, request):
        records = self.get_queryset()
        records_len = len(records)

        average = sum([rec.utilization_percent for rec in records]) / records_len

        return Response({"avg": average})

    @action(detail=False, methods=["GET"])
    def records_average(self, request):
        records = CpuInfoSlice.objects.all()
        records_len = len(records)

        average = sum([rec.utilization_percent for rec in records]) / records_len

        return Response({"avg": average})





