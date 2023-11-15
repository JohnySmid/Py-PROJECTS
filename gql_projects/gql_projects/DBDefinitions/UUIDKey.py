from sqlalchemy import Column, String

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