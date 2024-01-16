FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./asr_api.py /app

EXPOSE 8001

# CMD [ "python3", "asr_api.py"]

CMD [ "python3", "-m" , "flask", "--app", "asr_api", "run", "--host=0.0.0.0", "--port=8001"]