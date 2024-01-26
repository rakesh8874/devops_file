FROM python

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# # Use an official Python runtime as a parent image
# FROM python:3.8

# # Set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # Set the working directory in the container
# WORKDIR /app

# # Copy the requirements file into the container at /app
# COPY requirements.txt /app/

# # Install any needed packages specified in requirements.txt
# RUN pip install -r requirements.txt

# # Copy the current directory contents into the container at /app
# COPY . /app/

# # Port to expose
# EXPOSE 8000

# # Define environment variable for Django
# ENV DJANGO_SETTINGS_MODULE=basiccrud.settings

# # Command to run on container start
# CMD ["gunicorn", "basiccrud.wsgi:application", "--bind", "0.0.0.0:8000"]

# # # Base build
# # FROM python:3.10-alpine as base
# # RUN apk add --update --virtual .build-deps \
# #     build-base \
# #     postgresql-dev \
# #     python3-dev \
# #     libpq

# # COPY requirements.txt /app/requirements.txt
# # RUN pip install -r /app/requirements.txt

# # # Now multistage build
# # FROM python:3.10-alpine
# # RUN apk add libpq
# # COPY --from=base /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
# # COPY --from=base /usr/local/bin/ /usr/local/bin/
# # COPY . /app
# # ENV PYTHONUNBUFFERED 1

# # CMD ["gunicorn", "--reload", "--timeout=300", "--workers=2", "--worker-tmp-dir", "/dev/shm", "--bind=0.0.0.0:80", "--chdir", "/app/shop", "basiccrud.wsgi"]