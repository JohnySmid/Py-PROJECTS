from .UUIDColumn import UUIDColumn
from .UUIDKey import UUIDFKey
from . import BaseModel, Column, DateTime, String, ForeignKey, sqlalchemy, relationship

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