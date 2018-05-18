import datetime
from haystack import indexes
from .models import Mineral

class MineralIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    category = indexes.CharField(model_attr='category')


    def get_model(self):
        return Mineral


    def index_queryset(self, using=None):
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
