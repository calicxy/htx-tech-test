# htx-tech-test
*Note: The codes and commands were ran on a Windows laptop.

To set up a virtual environment:
1. python3 -m venv venv
To activate the virtual environment:
2. venv\Scripts\activate
To install the python packages in requirements.txt
3. pip install -r requirements.txt

## Task 2
To run Flask app asr_api directly (without Docker):
1. python3 ./asr/asr_api.py

To run the Docker container for the asr_api app:
1. cd asr
2. docker build --tag asr-api .
3. docker run -p 8001:8001 --name asr-api asr-api
Once done, to close the docker container:
4. docker stop asr-api
5. docker rm asr-api

## Task 3
The notebook for task 3a was done in Kaggle in order to utilise the GPU resources available on Kaggle. 
The link to the notebook is: https://www.kaggle.com/calistachoy/cv-train-2a-ipynb
A version of the notebook was downloaded and uploaded onto Github, with additional codes for the other parts added to the downloaded notebook.
The model checkpoint saved in a zip folder can be found here: https://drive.google.com/file/d/1qTGa3R-DbjSymraz-2xeW8vCCPf3Q5OW/view?usp=drive_link