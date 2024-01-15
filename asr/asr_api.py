from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
import torch
import librosa
import time
import numpy as np

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    if request.method == 'GET':
        return "pong"
    
@app.route('/asr', methods=['POST'])
def asr():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))

        # load model and processor
        processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-960h")
        model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h")

        y, sr = librosa.load(f.filename,  sr=16000)
        start_time = time.time()
        # tokenize
        input_values = processor(y, return_tensors="pt", padding="longest").input_values  # Batch size 1

        # retrieve logits
        logits = model(input_values).logits

        # take argmax and decode
        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = processor.batch_decode(predicted_ids)
        end_time = time.time()

        os.remove(secure_filename(f.filename))

        results_dict = {"transcription":transcription[0], "duration": str(np.round(end_time - start_time, 2))}
        return jsonify(results_dict)
        

if __name__ == '__main__':
    app.run(port=8001, 
            debug=True)