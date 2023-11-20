import strawberry as strawberryA
import typing
from typing import List, Annotated
from gql_projects.GraphResolvers import resolveFinancesForFinanceType, resolveFinanceTypeAll
from contextlib import asynccontextmanager

@asynccontextmanager
async def withInfo(info):
    asyncSessionMaker = info.context["asyncSessionMaker"]
    async with asyncSessionMaker() as session:
        try:
            yield session
        finally:
            pass

FinanceGQLModel = Annotated ["FinanceGQLModel",strawberryA.lazy(".FinanceGQLModel")]

from . import getLoaders

@strawberryA.federation.type(
    keys=["id"], description="""Entity representing a finance type"""
)
class FinanceTypeGQLModel:
    @classmethod
    async def resolve_reference(cls, info: strawberryA.types.Info, id: strawberryA.ID):
        loader = getLoaders(info).financetypes
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

    @strawberryA.field(description="""List of finances, related to finance type""")
    async def finances(
        self, info: strawberryA.types.Info
    ) -> typing.List["FinanceGQLModel"]:
        async with withInfo(info) as session:
            result = await resolveFinancesForFinanceType(session, self.id)
            return result
###########################################################################################################################
#
# Query 
#
###########################################################################################################################

@strawberryA.field(description="""Returns a list of finance types""")
async def finance_type_page(
    self, info: strawberryA.types.Info, skip: int = 0, limit: int = 10
) -> List[FinanceTypeGQLModel]:
    async with withInfo(info) as session:
        result = await resolveFinanceTypeAll(session, skip, limit)
        return result