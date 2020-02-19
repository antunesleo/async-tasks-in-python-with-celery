# async-tasks-in-python-with-celery
This repository is a reference to a medium story. This app is a first step with celery.


##### Setting up local:

`$ python first_app.py`
 
`$ celery -A celery_stuff.tasks worker -l debug -Q beer`

`$ celery -A celery_stuff.tasks worker -l debug -Q coffee`

##### Setting up with docker:

`$ docker-compose up --build`
