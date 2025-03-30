from flask import Flask, request, jsonify
from model_utils import recommend

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def get_recommendations():
    data = request.json
    user_input = data.get("preferences", [5, 300, 20, 10, 150])
    recommendations = recommend(user_input)
    return jsonify(recommendations.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
