from django.db import models
from django.core.exceptions import ValidationError


def validate_percent_min_max(percent: float):
    if percent > 100:
        raise ValidationError(f"{percent} percents greater than 100.0")
    elif percent < 0:
        raise ValidationError(f"{percent} percents less than 0.0")


class CpuInfoSlice(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    utilization_percent = models.FloatField(validators=[validate_percent_min_max])

    def __str__(self):
        return f"{self.created_at}: {self.utilization_percent}"

