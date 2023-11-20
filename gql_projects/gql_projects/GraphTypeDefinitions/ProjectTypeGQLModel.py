import uuid
import strawberry as strawberryA
import typing
from typing import List, Annotated
from . import  getLoaders
from contextlib import asynccontextmanager

@asynccontextmanager
async def withInfo(info):
    asyncSessionMaker = info.context["asyncSessionMaker"]
    async with asyncSessionMaker() as session:
        try:
            yield session
        finally:
            pass

from gql_projects.GraphResolvers import (
    resolveProjectsForProjectType,
    resolveProjectTypeAll
)

ProjectGQLModel = Annotated["ProjectGQLModel",strawberryA.lazy(".ProjectGQLModel")]


@strawberryA.federation.type(
    keys=["id"], description="""Entity representing a project types"""
)
class ProjectTypeGQLModel:
    @classmethod
    async def resolve_reference(cls, info: strawberryA.types.Info, id: strawberryA.ID):
        loader = getLoaders(info).projecttypes
        result = await loader.load(id)
        if result is not None:
            result._type_definition = cls._type_definition  # little hack :)
        return result

    @strawberryA.field(description="""Primary key""")
    def id(self) -> strawberryA.ID:
        return self.id

    @strawberryA.field(description="""Name""")
    def name(self) -> str:
        return self.name

    @strawberryA.field(description="""Name en""")
    def name_en(self) -> str:
        return self.name_en

    @strawberryA.field(description="""List of projects, related to project type""")
    async def projects(self, info: strawberryA.types.Info) -> typing.List["ProjectGQLModel"]:
        async with withInfo(info) as session:
            result = await resolveProjectsForProjectType(session, self.id)
            return result
        
###########################################################################################################################
#
# Query 
#
###########################################################################################################################

@strawberryA.field(description="""Returns a list of project types""")
async def project_type_page(
    self, info: strawberryA.types.Info, skip: int = 0, limit: int = 10
) -> List[ProjectTypeGQLModel]:
    async with withInfo(info) as session:
        result = await resolveProjectTypeAll(session, skip, limit)
        return result