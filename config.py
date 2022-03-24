import os
print(os.environ.get("POSTGRES_USER"))
user = os.environ.get("POSTGRES_USER")
password = os.environ.get("POSTGRES_PASSWORD")
host = os.environ.get("POSTGRES_HOST")
database = os.environ.get("POSTGRES_NAME")
port = os.environ.get("POSTGRES_PORT")

DATABASE_CONNECTION_URI = f'postgresql://{user}:{password}@{host}:{port}/{database}'
SECRET_KEY = 'secretkey'
print(DATABASE_CONNECTION_URI)