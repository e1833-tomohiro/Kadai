FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ADD requirements.txt /usr/src/app/
RUN pip install -r requirements.txt
ADD . /usr/src/app/
ADD manage.py ./user/src/app/
ADD index.html ./user/src/app/
ADD static ./user/src/app/static

CMD ["gunicorn",  "-k",  "geventwebsocket.gunicorn.workers.GeventWebSocketWorker",  "manage:resource", "-b", "0.0.0.0:5000"]
