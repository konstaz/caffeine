Docs:

1 create .env file : 
    - POSTGRES_USER = "coffee"
    - POSTGRES_PASSWORD = "coffee"
    - POSTGRES_HOST = "localhost" or "db" # depend how you're launching 
    - POSTGRES_NAME = "coffee"
    - POSTGRES_PORT = 5432

2 Create Dockerfile:

FROM python:3.9.5-slim-buster \
WORKDIR /usr/src/app \
RUN pip install --upgrade pip \
COPY ./requirements.txt /usr/src/app/requirements.txt \
RUN pip install -r requirements.txt \
COPY . .\
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"] \

3 Create docker-compose.yml :
version: '3.7'\

services:

  app:\
    build: .\
    ports:\
      - 5000:5000\
    env_file:\
      - ./.env\
    volumes:\
      - .:/code\
    depends_on:\
      - db\
  db:\
    image: postgres:13-alpine\
    ports:\
      - 5432:5432\
    env_file:\
      - ./.env\
    volumes:\
      - postgres_data:/var/lib/postgresql/data/\
    environment:\
      - POSTGRES_USER=coffee\
      - POSTGRES_PASSWORD=coffee\
      - POSTGRES_DB=coffee\

volumes:\
  postgres_data:\
  
4 docker-compose build app
5 docker-compose up -d

P.S. One can also launch app using python app.py \
Create in postgres respective Database:
CREATE DATABASE coffee; \
GRANT ALL PRIVILEGES ON DATABASE coffee TO coffee;

In case if migrations didn't applied automatically use: \
flask db init \
flask db migrate -m "Initial migration." \


List of endpoints:
- "01-signup"
- "02-login"
- "03-create-coffee-machine"
- "04-coffee-consumption-history"
- "05-coffee-purchase"
- "06-caffeine-level-statistic"
Data to send is explained in each file with a respective name
    