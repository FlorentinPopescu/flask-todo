"""
scripts to run to set up database
"""
from passlib.hash import pbkdf2_sha256

from datetime import datetime
from model import db, User, Task

# -------------------------------
# create the database tables for our model
db.connect()
db.drop_tables([User, Task])
db.create_tables([User, Task])

# -------------------------------
Task(name="Do the laundry.").save()
Task(name="Do the dishes.", performed=datetime.now()).save()

User(name="admin", password=pbkdf2_sha256.hash("password")).save()
User(name="florentin", password=pbkdf2_sha256.hash("florin")).save()

