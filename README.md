# Bitcoin Price Prediction

This project predicts Bitcoin's closing price based on historical data using machine learning.
Hosted [here](https://btc-closing-price-prediction.onrender.com/)

## Features
- Takes **opening price, closing price, and volume** for multiple consecutive days as input.
- Uses a **RandomForest** to predict the next closing price.
- Exposes an API endpoint to receive input data and return predictions.
- Provides a simple user interface to interact and predict BTC prices.

---

## Installation

### 1. Clone the Repository
```sh
git clone https://github.com/thesxm/btc-closing-price-prediction.git
cd btc-closing-price-prediction
```

### 2. Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Run the Application
Before running the application, you can optionally tweak the model by making changes in `model/model.ipynb`.

```sh
gunicorn api.app
```

The server will start on localhost.

---

## API Usage

### **Endpoint:** `POST /predict`
#### **Request Format (JSON)**
```json
[
    [open_day1, close_day1, volume_day1],
    [open_day2, close_day2, volume_day2],
    [open_day3, close_day3, volume_day3],
    [open_day4, close_day4, volume_day4]
]
```

#### **Response Format (JSON)**
```json
{
    "success": true,
    "predicted_closing_price": 51500.0
}
```

The server also provides a simple frontend to predict BTC prices.

---

## Approach
- The project uses a RandomForest to predict Bitcoin's closing price.
- A **sliding window approach** is applied, where the model takes **4** previous days' data (Opening Price, Closing Price and Volume) to predict the next day's price.
- The model is wrapped inside `ModelWrapper` to ensure correct input-output processing.
- The Flask API processes input, formats it, and returns the predicted price.

---
