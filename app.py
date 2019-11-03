from flask import Flask,jsonify,request,make_response
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)

# Returning the 
@app.route('/',methods=['POST'])
def indexing():
    return jsonify("yolo")
