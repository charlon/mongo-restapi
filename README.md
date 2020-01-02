# mongo_rest

VueJS client app. Django server with REST API using Pymongo. Mongo database.

## System Requirements

- Python (3+)
- Django (2+)
- Docker
- Node
- Mongo Compass (optional)

## Installation

Clone this repository

        $ git clone https://github.com/charlon/mongo-restapi

Go to your newly created repository

        $ cd mongo-restapi

## Configuration

Copy the sample .env file so that your environment can be run.

        $ cp .env.sample .env

# Development

## Docker

Docker/Docker Compose is used to containerize your local build environment and deploy it to an 'app' container which is exposed to your localhost so you can view your application. Docker Compose creates a 'devtools' container - which is used for local development. Changes made locally are automatically syncd to the 'app' container

        $ docker-compose up

In the case that changes are made to the Dockerfile or docker-compose.yml file, you will need to rebuild the image.

        $ docker-compose up --build

## MongoDB

The MongoDB server can be accessed using the following hostnames and default port.

        Internal: mongo_rest_db:27017
        External: localhost:27017

On the initial first build, 'mongo-volume' will be created and mounted. This volume will allow your database to persist for future builds. Delete this directory to clear your data.

Run Docker exec to bring up a bash console for your app container.

        $ docker exec -it mongo_rest_app /bin/bash

Activate virtualenv

        $ source bin/activate

Run the 'create_collection' managment command to create your empty collections.

        $ python manage.py create_collections

## Django

Django is used for both the backend API server and client app.

        API: http://localhost:8000/api/spots/

## Vue

Webpack watches for file changes and creates the bundles which is served from the client app (index.html).

        Vue: http://localhost:8000/


