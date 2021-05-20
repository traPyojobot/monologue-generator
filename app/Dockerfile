FROM python:3.8-alpine
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
RUN apk add build-base
ADD . /usr/src/app/
RUN pip install -r requirements.txt

CMD ["gunicorn", "main:app", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000"]