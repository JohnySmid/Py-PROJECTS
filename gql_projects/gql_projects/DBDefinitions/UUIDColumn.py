from . import BaseModel, Column, DateTime, String, ForeignKey, sqlalchemy, uuid, newUuidAsString


# Tyto funkce slouží k definici sloupců pro unikátní identifikátory (UUID) v tabulkách. 
# UUID je použito jako primární klíč pro některé tabulky. Funkce také umožňují určit, zda je sloupec cizího klíče (foreign key) a zda může být nullable.
def UUIDColumn(name=None):
    if name is None:
        return Column(String, primary_key=True, unique=True, default=newUuidAsString)
    else:
        return Column(
            name, String, primary_key=True, unique=True, default=newUuidAsString
        )