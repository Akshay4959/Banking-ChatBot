import numpy as np
from flask import Flask, request, render_template
import pickle
from project_final import bot_resp

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/',methods=['GET' , 'POST'])
def predict():
    user_input = " "
    if request.method == 'POST':
        user_input = request.form['user_input'].lower()
        bot_response = bot_resp(user_input)
        return render_template ('index.html' , bot_response)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run()