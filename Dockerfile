FROM tiangolo/uwsgi-nginx-flask:python3.8
COPY ./app /app
COPY ./requirements.txt .
WORKDIR /app/
RUN pip install -r requirements.txt
