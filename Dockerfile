FROM python:3.8-slim-buster

WORKDIR /asr

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "asr_api.py"]