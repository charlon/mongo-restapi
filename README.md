# mongo_rest

VueJS client app. Django server with REST API using Pymongo. Mongo database.

## System Requirements

- Python (3+)
- Django (2+)
- Docker
- Node
- Mongo Compass (application)

## Installation

Clone this repository

        $ git clone https://github.com/charlon/mongo-restapi

Go to your newly created repository

        $ cd mongo-restapi

## Configuration

Copy the sample .env file so that your environment can be run.

        $ cp .env.sample .env

## Development (using Docker)

Docker/Docker Compose is used to containerize your local build environment and deploy it to an 'app' container which is exposed to your localhost so you can view your application. Docker Compose creates a 'devtools' container - which is used for local development. Changes made locally are automatically syncd to the 'app' container

        $ docker-compose up

In the case that changes are made to the Dockerfile or docker-compose.yml file, you will need to rebuild the image.

        $ docker-compose up --build

View your Vue.js application

        Demo: http://localhost:8000/

## Mongo Compass

Connect to your Mongo database using the Mongo credentials specified in the '.env' file
