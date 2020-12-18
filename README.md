# Yoga app

## Backend
* Python 3.8
* Django 
* Postgres 12 

## Getting started 
### Install dependencies
`pip install -r requirements.txt`

### Bootstrap database
`python manage.py backfill`

### Run the webserver
`python manage.py runserver`

### Accessing the data via API

#### List poses
* Open browser at http://localhost:8000/poses/

#### Pose detail
* Open browser at http://localhost:8000/poses/<pose_id>/


