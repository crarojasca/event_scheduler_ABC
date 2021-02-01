FROM python:3.9

RUN git clone -b develop https://github.com/crarojasca/event_scheduler_ABC.git

WORKDIR /event_scheduler_ABC

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]