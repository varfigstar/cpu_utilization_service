from rest_framework import serializers

from .models import CpuInfoSlice


class CpuInfoSliceSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = CpuInfoSlice
        fields = [
            "id",
            "created_at",
            "utilization_percent",
        ]



