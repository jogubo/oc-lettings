FROM python:3.10.5-alpine AS oc-lettings

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY src .

RUN python manage.py collectstatic

COPY gunicorn.config.py .

ENTRYPOINT ["gunicorn"] 

CMD ["-c", "./gunicorn.config.py", "config.wsgi:application"] 
