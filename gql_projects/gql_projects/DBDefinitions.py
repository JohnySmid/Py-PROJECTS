# definice SQLAlchemy modelů, které mapují tabulky v databázi, a funkce pro inicializaci a konfiguraci databázového spojení
import sqlalchemy
import datetime

from sqlalchemy import (
    Column,
    String,
    BigInteger,
    Integer,
    DateTime,
    ForeignKey,
    Sequence,
    Table,
    Boolean,
    Float,
)
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import uuid

BaseModel = declarative_base()

def newUuidAsString():
    return f"{uuid.uuid1()}"

# Tyto funkce slouží k definici sloupců pro unikátní identifikátory (UUID) v tabulkách. 
# UUID je použito jako primární klíč pro některé tabulky. Funkce také umožňují určit, zda je sloupec cizího klíče (foreign key) a zda může být nullable.

# samostane v souboru
def UUIDColumn(name=None):
    if name is None:
        return Column(String, primary_key=True, unique=True, default=newUuidAsString)
    else:
        return Column(
            name, String, primary_key=True, unique=True, default=newUuidAsString
        )

# samostane v souboru
def UUIDFKey(*, ForeignKey=None, nullable=False):
    if ForeignKey is None:
        return Column(
            String, index=True, nullable=nullable
        )
    else:
        return Column(
            ForeignKey, index=True, nullable=nullable
        )
# id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("uuid_generate_v4()"),)

###########################################################################################################################
#
# zde definujte sve SQLAlchemy modely
# je-li treba, muzete definovat modely obsahujici jen id polozku, na ktere se budete odkazovat
#

# samostane v souboru
class ProjectModel(BaseModel):
    """
    Represents a project in the system.
    """
    __tablename__ = "projects"

    id = UUIDColumn()

    name = Column(String, comment="Name of the project")
    startdate = Column(DateTime, comment="Start date of the project")
    enddate = Column(DateTime, comment="End date of the project")

    projecttype_id = Column(ForeignKey("projecttypes.id"), index=True, comment="Foreign key referencing the project type")
    projecttype = relationship("ProjectTypeModel", back_populates="projects")

    group_id = UUIDFKey(nullable=True)#Column(ForeignKey("groups.id"), index=True)
    #group = relationship("groupModel")

    created = Column(DateTime, server_default=sqlalchemy.sql.func.now(), comment="Timestamp when the project was created")
    lastchange = Column(DateTime, server_default=sqlalchemy.sql.func.now(), comment="Timestamp of the last change to the project")
    createdby = UUIDFKey(nullable=True)#Column(ForeignKey("users.id"), index=True, nullable=True)
    changedby = UUIDFKey(nullable=True)#Column(ForeignKey("users.id"), index=True, nullable=True)

# samostane v souboru
class ProjectTypeModel(BaseModel):
    """
    Represents a type of project in the system.
    """
    __tablename__ = "projecttypes"

    id = UUIDColumn()
    name = Column(String, comment="Name of the project type")
    name_en = Column(String, comment="English name of the project type")

    category_id = Column(ForeignKey("projectcategories.id"), index=True, nullable=True, comment="Foreign key referencing the project category")
    projects = relationship("ProjectModel", back_populates="projecttype")

    created = Column(DateTime, server_default=sqlalchemy.sql.func.now(), comment="Timestamp when the project type was created")
    lastchange = Column(DateTime, server_default=sqlalchemy.sql.func.now(), comment="Timestamp of the last change to the project type")
    createdby = UUIDFKey(nullable=True)#Column(ForeignKey("users.id"), index=True, nullable=True)
    changedby = UUIDFKey(nullable=True)#Column(ForeignKey("users.id"), index=True, nullable=True)

# samostane v souboru
class ProjectCategoryModel(BaseModel):
    """
    Represents a category for projects in the system.
    """
    __tablename__ = "projectcategories"

    id = UUIDColumn()
    name = Column(String, comment="Name of the project category")
    name_en = Column(String, comment="English name of the project category")

    created = Column(DateTime, server_default=sqlalchemy.sql.func.now(), comment="Timestamp when the project category was created")
    lastchange = Column(DateTime, server_default=sqlalchemy.sql.func.now(), comment="Timestamp of the last change to the project category")
    createdby = UUIDFKey(nullable=True)#Column(ForeignKey("users.id"), index=True, nullable=True)
    changedby = UUIDFKey(nullable=True)#Column(ForeignKey("users.id"), index=True, nullable=True)

# samostane v souboru
class FinanceModel(BaseModel):
    """
    Represents financial information related to projects in the system.
    """
    __tablename__ = "projectfinances"

    id = UUIDColumn()
    name = Column(String, comment="Name of the financial information")
    amount = Column(sqlalchemy.types.DECIMAL(precision=13, scale=3), comment="Amount of the financial information")
    lastchange = Column(DateTime, server_default=sqlalchemy.sql.func.now(), comment="Timestamp of the last change to the financial information")

    project_id = Column(ForeignKey("projects.id"), index=True, comment="Foreign key referencing the associated project")

    financetype_id = Column(ForeignKey("projectfinancetypes.id"), index=True, comment="Foreign key referencing the financial information type")
    financetype = relationship("FinanceTypeModel", back_populates="finances")

    created = Column(DateTime, server_default=sqlalchemy.sql.func.now(), comment="Timestamp when the financial information was created")
    lastchange = Column(DateTime, server_default=sqlalchemy.sql.func.now(), comment="Timestamp of the last change to the financial information")
    createdby = UUIDFKey(nullable=True)#Column(ForeignKey("users.id"), index=True, nullable=True)
    changedby = UUIDFKey(nullable=True)#Column(ForeignKey("users.id"), index=True, nullable=True)

# samostane v souboru
class FinanceTypeModel(BaseModel):
    """
    Represents a type of financial information related to projects in the system.
    """
    __tablename__ = "projectfinancetypes"

    id = UUIDColumn()
    name = Column(String, comment="Name of the financial information type")
    name_en = Column(String, comment="English name of the financial information type")

    finances = relationship("FinanceModel", back_populates="financetype")

    created = Column(DateTime, server_default=sqlalchemy.sql.func.now(), comment="Timestamp when the financial information type was created")
    lastchange = Column(DateTime, server_default=sqlalchemy.sql.func.now(), comment="Timestamp of the last change to the financial information type")
    createdby = UUIDFKey(nullable=True)#Column(ForeignKey("users.id"), index=True, nullable=True)
    changedby = UUIDFKey(nullable=True)#Column(ForeignKey("users.id"), index=True, nullable=True)

# samostane v souboru
class FinanceCategory(BaseModel):
    """
    Represents a category for financial information related to projects in the system.
    """
    __tablename__ = "projectfinancecategories"

    id = UUIDColumn()
    name = Column(String, comment="Name of the financial information category")
    name_en = Column(String, comment="English name of the financial information category")

    created = Column(DateTime, server_default=sqlalchemy.sql.func.now(), comment="Timestamp when the financial information category was created")
    lastchange = Column(DateTime, server_default=sqlalchemy.sql.func.now(), comment="Timestamp of the last change to the financial information category")
    createdby = UUIDFKey(nullable=True)#Column(ForeignKey("users.id"), index=True, nullable=True)
    changedby = UUIDFKey(nullable=True)#Column(ForeignKey("users.id"), index=True, nullable=True)

# samostane v souboru
class MilestoneModel(BaseModel):
    """
    Represents a milestone for projects in the system.
    """
    __tablename__ = "projectmilestones"

    id = UUIDColumn()
    name = Column(String, comment="Name of the milestone")
    startdate = Column(DateTime, comment="Start date of the milestone")
    enddate = Column(DateTime, comment="End date of the milestone")

    project_id = Column(ForeignKey("projects.id"), index=True, comment="Foreign key referencing the associated project")

    created = Column(DateTime, server_default=sqlalchemy.sql.func.now(), comment="Timestamp when the milestone was created")
    lastchange = Column(DateTime, server_default=sqlalchemy.sql.func.now(), comment="Timestamp of the last change to the milestone")
    createdby = UUIDFKey(nullable=True)#Column(ForeignKey("users.id"), index=True, nullable=True)
    changedby = UUIDFKey(nullable=True)#Column(ForeignKey("users.id"), index=True, nullable=True)

# samostane v souboru
class MilestoneLinkModel(BaseModel):
    """
    Represents a link between milestones for projects in the system.
    """
    __tablename__ = "projectmilestonelinks"

    id = UUIDColumn()

    previous_id = Column(ForeignKey("projectmilestones.id"), index=True, nullable=True, comment="Foreign key referencing the previous milestone")
    next_id = Column(ForeignKey("projectmilestones.id"), index=True, nullable=True, comment="Foreign key referencing the next milestone")

    created = Column(DateTime, server_default=sqlalchemy.sql.func.now(), comment="Timestamp when the milestone link was created")
    lastchange = Column(DateTime, server_default=sqlalchemy.sql.func.now(), comment="Timestamp of the last change to the milestone link")
    createdby = UUIDFKey(nullable=True)#Column(ForeignKey("users.id"), index=True, nullable=True)
    changedby = UUIDFKey(nullable=True)#Column(ForeignKey("users.id"), index=True, nullable=True)

###########################################################################################################################

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine


async def startEngine(connectionstring, makeDrop=False, makeUp=True):
    """Provede nezbytne ukony a vrati asynchronni SessionMaker"""
    asyncEngine = create_async_engine(connectionstring)

    async with asyncEngine.begin() as conn:
        if makeDrop:
            await conn.run_sync(BaseModel.metadata.drop_all)
            print("BaseModel.metadata.drop_all finished")
        if makeUp:
            try:
                await conn.run_sync(BaseModel.metadata.create_all)
                print("BaseModel.metadata.create_all finished")
            except sqlalchemy.exc.NoReferencedTableError as e:
                print(e)
                print("Unable automaticaly create tables")
                return None

    async_sessionMaker = sessionmaker(
        asyncEngine, expire_on_commit=False, class_=AsyncSession
    )
    return async_sessionMaker


import os


def ComposeConnectionString():
    """Odvozuje connectionString z promennych prostredi (nebo z Docker Envs, coz je fakticky totez).
    Lze predelat na napr. konfiguracni file.
    """
    user = os.environ.get("POSTGRES_USER", "postgres")
    password = os.environ.get("POSTGRES_PASSWORD", "example")
    database = os.environ.get("POSTGRES_DB", "data")
    hostWithPort = os.environ.get("POSTGRES_HOST", "localhost:5432")

    driver = "postgresql+asyncpg"  # "postgresql+psycopg2"
    connectionstring = f"{driver}://{user}:{password}@{hostWithPort}/{database}"

    return connectionstring
