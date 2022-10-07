import datetime

from django.test import TestCase, Client

from .models import CpuInfoSlice
from .serializers import CpuInfoSliceSerializer


class CpuInfoSliceVewTestCase(TestCase):
    def setUp(self) -> None:
        self.slice_1 = CpuInfoSlice.objects.create(utilization_percent=55.0)
        self.slice_2 = CpuInfoSlice.objects.create(utilization_percent=44.23)

    def test_get_utilization_slices(self):
        expected_data = CpuInfoSliceSerializer(CpuInfoSlice.objects.order_by("-created_at"), many=True)

        client = Client()
        r = client.get("/api/cpu_info/")

        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json(), expected_data.data)
        self.assertGreater(len(r.json()), 0)

    def test_get_only_last_records(self):
        [CpuInfoSlice.objects.create(utilization_percent=55.0) for i in range(105)]
        client = Client()
        r = client.get("/api/cpu_info/")

        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 100)

    def test_post_utilization_slice(self):
        test_cases = [
            {"data": {"utilization_percent": 100.5}, "expected_code": 400},
            {"data": {"utilization_percent": -100}, "expected_code": 400},
            {"data": {"utilization_percent": 65.1}, "expected_code": 201},
        ]
        client = Client()
        for case in test_cases:
            r = client.post("/api/cpu_info/", data=case["data"])
            self.assertEqual(r.status_code, case["expected_code"])

    def test_last_records_average(self):
        CpuInfoSlice.objects.all().delete()
        now = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=-2)))
        slices = [CpuInfoSlice.objects.create(utilization_percent=i) for i in range(201)]
        for i, s in enumerate(slices):
            s.created_at = now + datetime.timedelta(hours=i)
            s.save()
        expected_data = 150.5
        client = Client()
        r = client.get("/api/cpu_info/last_records_average/")
        self.assertEqual(r.json()["avg"], expected_data)

    def test_records_average(self):
        CpuInfoSlice.objects.all().delete()
        now = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=-2)))
        slices = [CpuInfoSlice.objects.create(utilization_percent=i) for i in range(350)]
        for i, s in enumerate(slices):
            s.created_at = now + datetime.timedelta(hours=i)
            s.save()
        expected_data = 174.5
        client = Client()
        r = client.get("/api/cpu_info/records_average/")
        self.assertEqual(r.json()["avg"], expected_data)
