from Homepage import database, app
from Homepage.models import User

with app.app_context():
    database.create_all()

#import secrets
#print(secrets.token_hex(16))

