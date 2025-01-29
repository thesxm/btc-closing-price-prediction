import pandas as pd

class ModelWrapper:
    def __init__(self, model, window, input_columns, prediction_columns):
        self.model = model
        self.window = window
        self.input_columns = input_columns
        self.prediction_columns = prediction_columns

    def predict(self, x):
        # Validate data
        if len(x) != self.window + 1:
            raise BaseException(f"Invalid size of input x, {self.window + 1} rows required.")
        
        if list(x.columns) != self.input_columns:
            raise BaseException(f"Invalid columns in input x, expected columns are: {self.input_columns}")

        # Preprocess data
        for col in self.input_columns:
            x[f"{col}_Change"] = x[col].diff()
            x[f"{col}_Change_Ratio"] = x[f"{col}_Change"] / x[col]

        x = x.dropna().reset_index(drop = True)
        inp = pd.DataFrame(columns = [f"{c}_{w}" for c in self.prediction_columns for w in range(self.window)])
        inp.loc[0] = [x.at[len(x) - w - 1, c] for c in self.prediction_columns for w in range(self.window)]

        return self.model.predict(inp)[0]

    def predict_and_calculate_closing_price(self, x):
        previous_closing_price = x.at[len(x) - 1, "Close"]
        predicted_close_change_ratio = self.predict(x)

        return previous_closing_price / (1 - predicted_close_change_ratio)
