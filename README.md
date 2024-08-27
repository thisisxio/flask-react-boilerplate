# Flask-React-NextJs-PostgreSQL Boilerplate

Simple boilerplate for a fullstack application.

## Requirements

Before starting, make sure that your packages are up to date. If you are using HomeBrew, run:

`brew update`
`brew upgrade`

To make sure that you have installed python, postgres@14, run:

`brew services list`

### Set up your database

Assuming that you have installed Postres.

On your terminal, log into Postgres `sudo -iu postgres psql`

create your database: `CREATE DATABASE your_db_name;`

create database user: `CREATE USER sammy WITH PASSWORD 'password';`

## Environment Variables

Set up the following environment variables:

`FLASK_APP= run.py`
`FLASK_DEBUG=1`
`FLASK_ENV=development`
`POSTGRES_HOST=postgres`
`POSTGRES_PORT=5432`
` DATABASE_URL=postgresql://``USERNAME:PASSWORD@localhost:5432/your_db_name `

## Front End

- React
- NextJs
- Tailwind

## Back End

- Python/Flask
- PostgreSQL

### Install Packages

`pip3 install -r requirements.txt`

### Flask Migration

All models are located on /backend/app/models.py, modify them as you need.

Run these commands to create the Tables for your local db:

1. `flask db init`
2. `flask db migrate -m "MESSAGE"`
3. `flask db upgrade`

### Run Back End

1. Create virtual environment: `python -m venv myenv`
2. Activate environment: `source myenv/bin/activate`
3. Run application: `flask run`
