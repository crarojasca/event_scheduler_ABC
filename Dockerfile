FROM python:3.9

RUN git clone -b develop git@github.com:crarojasca/event_scheduler_ABC.git

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]