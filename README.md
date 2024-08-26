# flask-react-boilerplate

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
