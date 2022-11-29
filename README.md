# Command Storage Microservice

## Overview

This project was built for fun to encapsulate storing command references within a flask microservice.

Using this service, you'll be able to store command examples and references to an SQL database.

## Local Setup Guide

Before starting the setup process, please ensure you have Python/Anaconda and Docker installed and set up on your machine. Additionally, make sure you
have pip / conda configured. Once you have cloned the repo, please follow the following steps:

1. Activate venv / conda env.
    - To create a venv, simply run this command: `python -m venv <venv_name>`
    - For quick activation, run `./<venv_name>/Scripts/Activate.ps1`
2. Install all the dependencies using this command: `python -m pip install -r requirements.txt`

## Updating Dependencies

If any dependencies are updated, please be sure to update `requirements.txt`

To do this, run `pip freeze > requirements.txt` and then stash / commit your changes.

## Run the App

### Database Setup
In order for the API to run, you must add first initialize the database.

To do this, run the following prior to calling `flask run`:

`flask init-db`

### CMD

```
set FLASK_APP=flaskr
set FLASK_ENV=development
flask run
```

### Powershell

```
$env:FLASK_APP = "flaskr"
$env:FLASK_ENV = "development"
flask run
```

### Bash

```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```