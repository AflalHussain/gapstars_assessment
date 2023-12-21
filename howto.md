### Run postgres db
```docker-compose -f  docker-compose-db-setup.yml```

### Load DB changes
```bash
python manage.py makemigrations
python manage.py migrate
```

### Load Sample Data
```bash
python manage.py dumpdata Product --indent 2 > initial_data.json
python manage.py loaddata initial_data.json
```

### Start server
```bash
python manage.py runserver
```

### CHECK
You can use postman to test the functionalities of the app with th postman collection that I have added
`autocompany_requests.postman_collection.json`

