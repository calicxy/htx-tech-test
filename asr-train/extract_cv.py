import pandas as pd
import zipfile
import os

df = pd.read_csv("asr/cv-valid-dev.csv")

with zipfile.ZipFile("asr/common_voice.zip", "r") as f:
    for id, row in df.iterrows():
        if os.path.exists('cv-valid-dev/'+row["filename"]):
            continue
        else:
            f.extract('cv-valid-dev/'+row["filename"])
        