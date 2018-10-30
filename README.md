absolute zero sugar, thats what the label says
===================
## Description
 - Something to do with attendance.

------------------------------------------------------------------------

## Getting started
### Requirements
* Python 3.6 +

### Creating a virtual environment
 * You can use virtualenvwrapper / virtualenv or whatever virtual environment tool you use

### Installing dependencies
```bash
pip3 install -r requirements.txt
```

### Prepare environmet variables
* For this project you will need the following configurations.
```bash
export SECRET_KEY=some pseudo random characters
```


### Running the server 
```bash
#development server
python manage.py runserver

#production server
gunicorn 'app:create_app()' --access-logfile access.log --error-logfile error.log
```

#### Create fake users
- To test api endpoint using the json below you first need some data of allowed items in the db:
```bash
python manage.py fake_users -n 'number of fake users'
```

### Testing the api endpoints
* Use any tool you wish like curl, postman, browser ...

#### Retrieve user endpoint
`/api/v1/get-user/<user_id>`
- returns json structure
```json
{
    "name":"username",
    "class":"name of class",
    "image":"url to image",
}
```

### Running the tests
```bash
python manage.py test
```
