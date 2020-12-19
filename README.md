# Yoga app

## Backend
* Python 3.8
* Django 
* Postgres 12 

## Getting started 
### Install dependencies
```shell
pip install -r requirements.txt
```

### Bootstrap database
```shell
createdb yoga
python manage.py migrate
python manage.py backfill
```

### Running frontend
```shell
cd frontend
npm install
npm start
```

### Run the webserver
```shell
python manage.py runserver
```

### Accessing the data via API

#### List poses
* Open browser at http://localhost:8000/poses/

#### Pose detail
* Open browser at http://localhost:8000/poses/<pose_id>/


