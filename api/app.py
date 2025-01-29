import joblib
import logging
import pandas as pd
from flask import Flask, request, jsonify, render_template

def create_app():
    app = Flask(__name__)
    model = joblib.load("model/model.pkl")

    logger = logging.getLogger()

    @app.get("/")
    def index():
        return render_template("index.html")

    @app.post("/predict")
    def predict():
        try:
            x = pd.DataFrame(request.json, columns = model.input_columns)
        except:
            return jsonify({
                "success": False,
                "error": f"Bad payload, input of shape ({model.window + 1}, {len(model.input_columns)}) required, columns following the order {model.input_columns}."
                }), 400

        try:
            predicted_price = model.predict_and_calculate_closing_price(x)
        except BaseException as e:
            logger.error(f"Error predicting closing price: {str(e)}")

            return jsonify({
                "success": False,
                "error": "Failed to predict closing price."
                })

        return jsonify({
            "success": True,
            "predicted_price": predicted_price
            }), 200

    return app

application = create_app()
