FROM python:3.10.5-slim-bullseye AS oc-lettings

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY src .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
