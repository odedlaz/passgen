FROM python:3-alpine
ADD . /app
RUN pip install -r /app/requirements.txt
EXPOSE 80
CMD ["python", "-u", "/app/passgen.py"]
