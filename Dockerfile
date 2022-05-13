FROM tiangolo/uwsgi-nginx-flask:python3.8
COPY ./app /app
COPY ./requirements.txt .
#WORKDIR /app/
RUN pip install -r requirements.txt
#RUN apk --update add bash nano
#ENV STATIC_URL /static
#ENV STATIC_PATH /var/www/app/static