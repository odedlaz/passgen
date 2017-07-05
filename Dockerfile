FROM python:3-alpine
ADD . /app
RUN apk add --update g++
RUN pip install -r /app/requirements.txt
EXPOSE 80

WORKDIR /app
CMD gunicorn -b 0.0.0.0:80 \
             --worker-class gevent \
             --workers 2 \
             --max-requests 1000 passgen:app
