# htx-tech-test
*Note: The codes and commands are run on a Windows laptop.

To set up a virtual environment:
1. python3 -m venv venv
To activate the virtual environment:
2. venv\Scripts\activate
To install the python packages in requirements.txt
3. pip install -r requirements.txt

To run Flask app asr_api directly (without Docker):
1. python3 ./asr/asr_api.py

To run the Docker container for the asr_api app:
1. cd asr
2. docker build --tag asr-api .
3. docker run -p 8001:8001 --name asr-api asr-api
Once done, to close the docker container:
4. docker stop asr-api
5. docker rm asr-api