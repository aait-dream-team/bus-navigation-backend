FROM python:3.8
ENV PYTHONUNBUFFERED 1

# Allows docker to cache installed dependencies between builds
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Adds our application code to the image
COPY . code
WORKDIR /code

EXPOSE 8000

# Run the server
CMD python wait_for_postgres.py && ./manage.py migrate && ./manage.py runserver 0.0.0.0:8000
