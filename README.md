### Running the api with docker

```docker-compose up -d```

#### Test the endpoints
You can use postman to test the functionalities of the app with th postman collection that I have added
`autocompany_requests.postman_collection.json`



### Running the api without docker

#### Run postgres db
```docker-compose up postgres -d```

#### Create Virtual Environment
```python -m venv venv```

#### Activate Virtual Environment
```. venv/bin/activate```

#### Install Requirments
```pip install -r requirements.txt```

#### Load DB changes
```bash
python manage.py makemigrations sales_app
python manage.py migrate
```

#### Load Sample Data
```bash
python manage.py loaddata initial_data.json
```

#### Start server
```bash
python manage.py runserver
```

#### Test the endpoints
You can use postman to test the functionalities of the app with th postman collection that I have added
`autocompany_requests.postman_collection.json`

