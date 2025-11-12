from sqlalchomy import create_engine, Metadata
import uuid 
from datetime import datetime, timezone 

engine = create_engine("postgresql://scott:tiger@localhost/mydatabase")
metadata = Metadata()
metadata.create_all(bind=engine)

new uuid = uuid.uuid4()
now = datetime.now(timezone("utc"))
