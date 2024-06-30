### Milestone 2
create dockerfile for the backend
**repository:** https://github.com/IbrahimHanyEl-Sheikh/simple-django-app
- choose the suitable base image to build your custom image on top of it.
- install dependency like packages in the python virtual environment.
- add environment variable called **PYTHONUNBUFFERED** and set its value to **1**
- start create the schemas in the database. using python command
```python
# depends on the python version you used in the base image for example here we use latest python3 version
python manage.py makemigrations
```
- then migrate default data in the tables using python command
```python
# depends on the python version you used in the base image for example here we use latest python3 version
 python3 manage.py migrate
 ```
 - last step to run the django server and expose the server on port 8090 using command
 ```python
 # depends on the python version you used in the base image for example here we use latest python3 version
 python3 manage.py runserver
 ```
 ##### Note
 - ensure that after building the image and run container that we can access the API using curl or any application (like postman) for testing that API can be reachable.
- if there is issue to reach out the API try to check if the container is exposed or not?
- if you have docker or podman installed on the local laptop or if you are using the VM run the project on visual studio code on the VM.

create dockerfile for the frontend
**repository:** https://github.com/IbrahimHanyEl-Sheikh/simple-react-app

- choose the suitable base image to build your custom image on top of it to work with node js.
- install dependency packages.
- try to build the project if the built fail check if the whole project content copied to the image or not. you need to have all files to build the project.
- build the htmls for the web application.
- run the server with the default values.
##### Note
 - ensure that after building the image and run container after exposing the right port that you can access the default page in the url example localhost:3000. 
 - if you have docker or podman installed on the local laptop or if you are using the VM run the project on visual studio code on the VM.
