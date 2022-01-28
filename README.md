# Flowork

Flowork is my attempt at a basic workflow orchestration backend. I gave it a name because the project needed a name.

## Project Setup

The project is designed to have well-separated definitions between development/local and production or any other deployment environment. The local environment variables are stored in the repo, however, the expectation is the production environment will have its environment variables defined in a secure location and subsequently made available to the application either through a generated file, or on the host (eg. bundled image on host).

The project is run using [Pipenv](https://pipenv.pypa.io/en/latest/), which you're free to install using the instructions from the docs. It is the project's de facto package manager and virtual environment manager. It will encapsulate the environment for the project, from the OS. You can initialise the environment and install packages using:

`pipenv install`

After installing the project, you can run it using the Django local server command, which will make the application available on [localhost](http://localhost:8000/), port 8000:

`make dev`

## The assignment

Once the server is running, you can access the requested view [here](http://localhost:8000/worklows/report/). From there, you can use the bog standard front-end to request a CSV.

Dummy data can be loaded from the fixtures in the repo with the command:

`python manage.py loaddata db.json`

## Test

More of an example of testing than an exhaustive suite, the test can be run with the following command:

`make test`

## Bonus work

The code for a [DRF](https://www.django-rest-framework.org/)-based API is located in `workflows/api`, though none of it is connected to anything. I thought this was good enough for "some code". It's untested but shouldn't be too far off from a complete solution.
