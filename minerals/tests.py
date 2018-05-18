from django.urls import reverse
from django.test import TestCase
from django.utils import timezone

from .models import Mineral

class MineralModelsTests(TestCase):
    def test_mineral_creation(self):
        mineral = Mineral.objects.create(
            name="Filipovic",
            group="organic"
        )
        self.assertEqual(mineral.name, "Filipovic")
        self.assertEqual(mineral.group, "organic")


class CourseViewTests(TestCase):
    def setUp(self):
        self.mineral1 = Mineral.objects.create(
            name="Alchanic",
            group="Organic",
            color="blue",
            unit_cell=5
        )
        self.mineral2 = Mineral.objects.create(
            name="Brambora",
            group="Non-organic",
            color="red",
            unit_cell=10
        )

    def test_mineral_list_view(self):
        response = self.client.get(reverse('minerals:index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.mineral1, response.context['all_entries'])
        self.assertIn(self.mineral2, response.context['all_entries'])
        self.assertTemplateUsed(response, 'minerals/index.html')
        self.assertContains(response, self.mineral1.name)

    def test_mineral_detail_view(self):
        response = self.client.get(reverse('minerals:detail', kwargs={'pk': self.mineral2.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'minerals/detail.html')
        self.assertContains(response, self.mineral2.name)
