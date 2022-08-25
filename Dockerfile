FROM python:3.10.1
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y postgresql-contrib
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY docker_commands.sh .
RUN chmod +x docker_commands.sh
COPY . /code/
RUN pip install gunicorn
