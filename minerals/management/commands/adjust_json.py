from django.core.management.base import BaseCommand, CommandError

import json

CAPTIONS = [
"name", "image_filename", "image_caption", "category", "formula",
"strunz_classification", "color", "crystal_system", "unit_cell",
"crystal_symmetry", "cleavage", "mohs_scale_hardness", "luster", "streak",
"diaphaneity", "optical_properties", "refractive_index", "crystal_habit",
"specific_gravity", "group"
]
FILENAME = "minerals.json"


class Command(BaseCommand):
    """ Adjusts JSON """
    help = "Adjusts JSON"

    def add_arguments(self, parser):
        pass


    def handle(self, *args, **options):
        # opens json file from Treehouse
        with open(FILENAME, encoding='utf-8') as file:
            datas = json.load(file)
        # adds empty captions
        for data in datas:
            for each in CAPTIONS:
                try:
                    data[each]
                except KeyError:
                    data[each] = ""
        # export dics to new JSON file
        with open('minerals2.json', 'w') as fp:
            json.dump(datas, fp)
        self.stdout.write(
        self.style.SUCCESS('JSON file has been successfully changed!'))
