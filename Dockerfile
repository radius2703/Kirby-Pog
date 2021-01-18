FROM python:3.8.7-buster

WORKDIR /KirbyPog

COPY . /KirbyPog

RUN pip install -r requirements.txt

CMD python ./bot.py
