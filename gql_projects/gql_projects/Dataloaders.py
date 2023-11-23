# efektivní načítání dat z databáze, třída Loaders obsahuje vlastnosti pro načítací funkce pro jednotlivé modely, 
# a tyto načítací funkce jsou optimalizovány pro efektivní práci s databází a snižují počet dotazů na databázi.
# from uoishelpers.dataloaders import createIdLoader, createFkeyLoader
# from sqlalchemy import select
# from functools import cache

# from gql_projects.DBDefinitions import (
#     ProjectCategoryModel,
#     ProjectTypeModel,
#     ProjectModel,
#     MilestoneModel,
#     MilestoneLinkModel,
#     FinanceCategory,
#     FinanceTypeModel,
#     FinanceModel
# )
# from uoishelpers.dataloaders import createIdLoader

# def createLoader(asyncSessionMaker):
#     class Loaders:
#         @property
#         @cache
#         def project_by_id(self):
#             return createIdLoader(asyncSessionMaker, ProjectModel)

#         @property
#         @cache
#         def project_page(self):
#             return createIdLoader(asyncSessionMaker, ProjectModel)

#         @property
#         @cache
#         def finance_by_id(self):
#             return createIdLoader(asyncSessionMaker, FinanceModel)

#         @property
#         @cache
#         def project_type_page(self):
#             return createIdLoader(asyncSessionMaker, ProjectTypeModel)

#         @property
#         @cache
#         def finance_page(self):
#             return createIdLoader(asyncSessionMaker, FinanceModel)

#         @property
#         @cache
#         def finance_type_page(self):
#             return createIdLoader(asyncSessionMaker, FinanceTypeModel, foreignKeyName="facility_id")

#         @property
#         @cache
#         def milestone_page(self):
#             return createIdLoader(asyncSessionMaker, MilestoneModel)

#         @property
#         @cache
#         def project_by_group(self):
#             return createIdLoader(asyncSessionMaker, ProjectModel)

#         @property
#         @cache
#         def project_category(self):
#             return createIdLoader(asyncSessionMaker, ProjectCategoryModel)

#         @property
#         @cache
#         def finance_category(self):
#             return createIdLoader(asyncSessionMaker, FinanceCategory)

#     return Loaders()


# from gql_projects.DBDefinitions import (
#     ProjectCategoryModel,
#     ProjectTypeModel,
#     ProjectModel,
#     MilestoneModel,
#     MilestoneLinkModel,
#     FinanceCategory,
#     FinanceTypeModel,
#     FinanceModel
# )

# #slovník, názvy modelů a odpovídající třídy modelů databáze. Tyto třídy reprezentují různé tabulky nebo entity v databázi.
# dbmodels = {
#     "projectcategories": ProjectCategoryModel,
#     "projecttypes": ProjectTypeModel,
#     "projects": ProjectModel,
#     "milestones": MilestoneModel,
#     "milestonelinks": MilestoneLinkModel,
#     "financecategory": FinanceCategory,
#     "financetypes": FinanceTypeModel,
#     "finances": FinanceModel
# }
# #Tato funkce slouží k vytvoření načítacích funkcí pro jednotlivé modely.
# async def createLoaders(asyncSessionMaker, models=dbmodels):
#     #Tato funkce vytváří a vrací lambda funkci, která slouží k vytvoření konkrétního datového načítace pro určitý model.
#     def createLambda(loaderName, DBModel):
#         return lambda self: createIdLoader(asyncSessionMaker, DBModel)
    
#     attrs = {}
#     for key, DBModel in models.items():
#         attrs[key] = property(cache(createLambda(key, DBModel)))
    
#     Loaders = type('Loaders', (), attrs)   
#     return Loaders()

# from functools import cach