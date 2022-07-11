FROM python:3.8

RUN mkdir /app
COPY /DRF_practice /app

RUN pip install -r /app/requirements.txt
EXPOSE 8000
WORKDIR /app
#CMD ["python", "-m", "django", "run", "--host=0.0.0.0"]