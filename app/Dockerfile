FROM python:3.7-alpine
WORKDIR /myapp
COPY . /myapp
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev


RUN pip install -r requirements.txt
EXPOSE 80
CMD ["python", "myapp.py"]
