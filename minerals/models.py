from django.db import models


class Mineral(models.Model):
    name = models.TextField()
    image_filename = models.TextField()
    image_caption = models.TextField()
    category = models.TextField()
    formula = models.TextField()
    strunz_classification = models.TextField()
    color = models.TextField()
    crystal_system = models.TextField()
    unit_cell = models.TextField()
    crystal_symmetry = models.TextField()
    cleavage = models.TextField()
    mohs_scale_hardness = models.TextField()
    luster = models.TextField()
    streak = models.TextField()
    diaphaneity = models.TextField()
    optical_properties = models.TextField()
    refractive_index = models.TextField()
    crystal_habit = models.TextField()
    specific_gravity = models.TextField()
    group = models.TextField()
    pub_date = models.DateTimeField(default="1990-01-25 00:00:00")

    class Meta:
        ordering = ['name']

    # converts DB values to string
    def __str__(self):
        return self.name
