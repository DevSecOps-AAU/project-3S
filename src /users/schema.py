from sqlalchomy import Metadata, Table, Column, Integer, String, Datetime, Enum
from uuid(as_uuid=True) import uuid(as_uuid=True)

users= Table(
    "users", metadata,
    column("id", uuid(as_uuid=True), primary_key=True),
    column("username", String(50), nullable=False),
    column("email", String(100), unique=True),
    column("password", String(100), unique=True),
    column("created_at",Datetime),
    column("updated_at",Datetime),
    
)

favorites= Table(
    "favorites", metadata,
    column("id", uuid(as_uuid=True), primary_key=True),
    column("user_id", uuid(50), nullable=False),
    column("place_id",uuid(as_uuid=True), primary_key=True),
    column("created_at",Datetime),
    column("updated_at",Datetime),
    
)

 places= Table(
    "places", metadata,
    column("id", uuid(as_uuid=True), primary_key=True),
    column("name", uuid(50), nullable=False),
    column("description", String(100), unique=True),
    column("location", String(50), nullable=False),
     column("features", String(50), nullable=False),
    column("created_at",Datetime),
    column("updated_at",Datetime),
    
)


 recommended_place= Table()
    "recommended_place", metadata,
    column("id", uuid(as_uuid=True), primary_key=True),
    column("place_id", uuid(as_uuid=True, primary_key=True),
    column("title", String(50), nullable=False),
    column("description", String(100), unique=True),
    column("datetime", Datetime),
    column("created_at",Datetime),
    column("updated_at",Datetime),
    
)
