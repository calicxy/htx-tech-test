import pandas as pd
from datasets import load_metric

wer_metric = load_metric("wer")

df = pd.read_csv("asr-train/cv-valid-dev_transcribed.csv")
# print(df.head())

predictions = df["generated_text"].apply(lambda x: str(x).lower()).values
reference = df["text"].values
    
print(wer_metric.compute(predictions=predictions, references=reference))
# WER = 0.10825

ft_df = pd.read_csv("asr-train/cv-valid-dev_finetuned.csv")

predictions = ft_df["generated_text"].apply(lambda x: str(x).lower()).values
reference = ft_df["text"].apply(lambda x: str(x).lower()).values

print(wer_metric.compute(predictions=predictions, references=reference))
# WER = 0.10596