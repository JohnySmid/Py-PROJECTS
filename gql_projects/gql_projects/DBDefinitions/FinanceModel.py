from UUIDColumn import BaseModel, UUIDColumn, Column, DateTime, String, ForeignKey, sqlalchemy, relationship
from UUIDKey import UUIDFKey

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