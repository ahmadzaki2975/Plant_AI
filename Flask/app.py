from flask import Flask, render_template, jsonify, request, Markup
from model import predict_image
import utils
from flask_cors import CORS
from PIL import Image
import requests
import io
import PIL
import webbrowser

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            file = request.files['file']
            img = file.read()
            prediction = predict_image(img)
            print(prediction)
            res = Markup(utils.disease_dic[prediction])
            print(res)
            return res
        except:
            print("error")
            return "error"
            pass
    return render_template('index.html', status=500, res="Internal Server Error")
    return "error"


if __name__ == "__main__":
    app.run(debug=True)
