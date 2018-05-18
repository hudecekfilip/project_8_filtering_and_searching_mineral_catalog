from django.core.management.base import BaseCommand, CommandError
from minerals.models import Mineral

import json


filename = 'minerals2.json'


class Command(BaseCommand):
    """ Adds minerals data from minerals.json to the sqlite3 database """
    help = "Adds JSON data to database"

    def add_arguments(self, parser):
        pass


    def handle(self, *args, **options):
        with open(filename, encoding='utf-8') as file:
            datas = json.load(file)

        for mineral in datas:
            Mineral(
                name = mineral['name'],
                image_filename = mineral['image_filename'],
                image_caption = mineral['image_caption'],
                category = mineral['category'],
                formula = mineral['formula'],
                strunz_classification = mineral['strunz_classification'],
                crystal_system = mineral['crystal_system'],
                unit_cell = mineral['unit_cell'],
                color = mineral['color'],
                crystal_symmetry = mineral['crystal_symmetry'],
                cleavage = mineral['cleavage'],
                mohs_scale_hardness = mineral['mohs_scale_hardness'],
                luster = mineral['luster'],
                streak = mineral['streak'],
                diaphaneity = mineral['diaphaneity'],
                optical_properties = mineral['optical_properties'],
                refractive_index = mineral['refractive_index'],
                crystal_habit = mineral['crystal_habit'],
                specific_gravity = mineral['specific_gravity']
            ).save()
        self.stdout.write(self.style.SUCCESS(
            'Mineral data has been successfully added!'))
