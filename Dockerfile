FROM python:3.11.1-alpine3.17

ENV PYTHONUNBUFFERED 1 

WORKDIR /app
RUN pip install django

COPY ./ ./

ENV PORT 8000

CMD python manage.py runserver --workers 1 --threads 8 app:app