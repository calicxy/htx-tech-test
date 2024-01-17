import os
import requests
import pandas as pd
import zipfile
import torch
import librosa

df = pd.read_csv("asr/cv-valid-dev.csv")

transcriptions = []

with zipfile.ZipFile("asr/common_voice.zip", "r") as f:

    for id, row in df.iterrows():
        if os.path.exists('cv-valid-dev/'+row["filename"]):
            continue
        else:
            f.extract('cv-valid-dev/'+row["filename"])

        url = 'http://127.0.0.1:8001/asr'
        files = {'file': open('cv-valid-dev/'+row["filename"], 'rb')}
        r = requests.post(url=url, files=files)
        # print(r.text)
        transcriptions.append(r.json()['transcription'])
        
df["generated_text"] = transcriptions
df.to_csv("asr/cv-valid-dev_transcribed.csv", index=False)

