from UUIDColumn import BaseModel, UUIDColumn, Column, DateTime, String, ForeignKey, sqlalchemy
from UUIDKey import UUIDFKey

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