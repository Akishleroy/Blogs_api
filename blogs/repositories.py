from typing import Protocol,OrderedDict
from blogs import models
from django.db.models import QuerySet
class BlogRepositoriesInterface(Protocol):

    def create_blog(self,data:OrderedDict)->models.Blog: ...

    def get_blogs(self)->QuerySet[models.Blog]:...

class BlogRepositoriesV1:
    def create_blog(self,data:OrderedDict)->models.Blog:
        return models.Blog.objects.create(**data)

    def get_blogs(self)->QuerySet[models.Blog]:
        return models.Blog.objects.all()
