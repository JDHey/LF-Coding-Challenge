FROM python:3.6.5
WORKDIR /anonymize
COPY . .
ENTRYPOINT ["python", "./run.py"]