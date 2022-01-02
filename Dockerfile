# Credits to https://www.section.io/engineering-education/django-docker/

# pull the 3.10.1 buster tag of python
FROM python:3.10.1-buster

# create app directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# copy project
COPY auth_demo /usr/src/app

# expose port 8000 
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
