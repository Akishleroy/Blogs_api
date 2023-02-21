from typing import Protocol, OrderedDict
from blogs import models, repositories
from django.db.models import QuerySet


class BlogServicesInterface(Protocol):
    repos: repositories.BlogRepositoriesInterface

    def create_blog(self, data: OrderedDict) -> models.Blog: ...

    def get_blogs(self) -> QuerySet[models.Blog]: ...


class BlogServicesV1:
    repos: repositories.BlogRepositoriesInterface = repositories.BlogRepositoriesV1

    def create_blog(self, data: OrderedDict) -> models.Blog:
        print("created in service layer")
        return self.repos.create_blog(self, data=data)

    def get_blogs(self) -> QuerySet[models.Blog]:
        return self.repos.get_blogs(self)
