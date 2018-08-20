FROM python:3.6.5-stretch

RUN mkdir /rmc
WORKDIR /rmc

ADD . .

RUN pip install pipenv
RUN pipenv sync

CMD pipenv run python run.py
