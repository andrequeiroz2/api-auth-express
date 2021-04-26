FROM python:3.9
#nikolaik/python-nodejs:latest
#

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt requirements.txt

RUN python -m pip install pip==21.0.1 &&\
    pip install --no-cache-dir -r requirements.txt

# copy project
COPY . .

#port
EXPOSE 6010

#run gnicorn
CMD ["gunicorn", "-w", "4", "--bind", "0.0.0.0:6010", "app:create_app()"]