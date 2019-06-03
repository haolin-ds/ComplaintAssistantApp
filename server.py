from flask import Flask, request, render_template, jsonify
#import model_cos
from ComplaintsAnalysis.Predictor import Predictor

app = Flask(__name__)

#prepare the model
predictor = Predictor()
print('model is ready')

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/predictions", methods=['POST'])
def predictions():
    """
    data = request.json
    print('##### start getting recommendations')
    rec = model.get_recommendations(data)
    print('##### done getting recommendations')

    """
    narrative = request.args.get('narrative')
    print(narrative)
    product_type, escalation_prob_fig, suggest_response = predictor.predict(narrative)
    result = {}
    result["product_type"] = product_type
    result["escalation_prob"] = escalation_prob_fig
    result["suggested_response"] = suggest_response
    return jsonify(result)
    #return jsonify(rec)

if __name__ == '__main__':  # Script executed directly
    app.run(host='0.0.0.0', port = 8080, debug=False)
    