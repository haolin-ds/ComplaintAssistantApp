# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, render_template, request

# Create the application object
from ComplaintsAnalysis.Predictor import Predictor

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

# prepare the model
predictor = Predictor()
print('model is ready')

@app.route('/',methods=["GET", "POST"])
def home_page():
    return render_template('index.html')  # render a template

@app.route('/predict')
def predict():
    # Pull input
    narrative =request.args.get('user_input')

    # Case if user input is empty
    if narrative == '':
        return render_template("index.html",
                              user_input="Empty")
    else:
        product_type, escalation_prob_fig, suggest_response, probs = predictor.predict(narrative)

        #print(product_type)
        escalation_prob_fig = escalation_prob_fig.split("/")[1]
        #print(escalation_prob_fig)
        suggest_response = suggest_response.split("_")[-1]
        #print(suggest_response)

        will_escalate = 0
        for prob in probs:
            if prob > 0.5:
                will_escalate = 1

        return render_template("index.html",
                              product_type=product_type,
                              escalation_prob_img=escalation_prob_fig,
                              suggest_response=suggest_response,
                              narrative=narrative,
                              will_escalate= will_escalate,
                              user_input="NotEmpty")


# start the server with the 'run()' method
if __name__ == "__main__":
    app.run(debug=False) #will run locally http://127.0.0.1:5000/

@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response