from .UUIDColumn import UUIDColumn
from .UUIDKey import UUIDFKey
from . import BaseModel, Column, DateTime, String, ForeignKey, sqlalchemy, relationship

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