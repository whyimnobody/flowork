# Flowork

Flowork is my attempt at a basic workflow orchestration backend. I gave it a name because the project needed a name.

## Project Setup

The project is designed to have well-separated definitions between development/local and production or any other deployment environment. The local environment variables are stored in the repo, however, the expectation is the production environment will have its environment variables defined in a secure location and subsequently made available to the application either through a generated file, or on the host (eg. bundled image on host).

The project is run using [Pipenv](https://pipenv.pypa.io/en/latest/), which you're free to install using the instructions from the docs. It is the project's de facto package manager and virtual environment manager. It will encapsulate the environment for the project, from the OS. You can initialise the environment and install packages using:

`pipenv install`

After installing the project, you can run it using the Django local server command, which will make the application available on [localhost](http://localhost:8000/), port 8000:

`python manage.py runserver`

## The assignment

Once the server is running, you can access the requested view [here](http://localhost:8000/worklow/download-csv/). From there, you can use the bog standard front-end to request a CSV.
