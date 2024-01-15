from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    if request.method == 'GET':
        return "pong"
    
@app.route('/asr', methods=['GET', 'POST'])
def asr():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        results_dict = {"transcription":"BEFORE HE ...", "duration":"20.7"}
        return jsonify(results_dict)
        

if __name__ == '__main__':
    app.run(port=8001, 
            debug=True)