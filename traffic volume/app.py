from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

app = Flask(__name__)

np.random.seed(42)

hours = np.random.randint(0, 24, 500)
temperature = np.random.randint(20, 45, 500)
weather = np.random.randint(0, 2, 500)
day = np.random.randint(0, 7, 500)
month = np.random.randint(1, 13, 500)
holiday = np.random.randint(0, 2, 500)
road_type = np.random.randint(0, 3, 500)

traffic_volume = (
    (hours * 40) +
    (temperature * 10) +
    (weather * 100) +
    (day * 30) +
    (month * 15) +
    (holiday * -200) +
    (road_type * 120)
)

traffic_data = pd.DataFrame({
    'hour': hours,
    'temperature': temperature,
    'weather': weather,
    'day': day,
    'month': month,
    'holiday': holiday,
    'road_type': road_type,
    'traffic_volume': traffic_volume
})

X = traffic_data[[
    'hour','temperature','weather','day','month','holiday','road_type'
]]
y = traffic_data['traffic_volume']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor()
model.fit(X_train, y_train)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    hour = int(request.form['hour'])
    temperature = int(request.form['temperature'])
    weather = int(request.form['weather'])
    day = int(request.form['day'])
    month = int(request.form['month'])
    holiday = int(request.form['holiday'])
    road_type = int(request.form['road_type'])

    prediction = model.predict([[hour, temperature, weather, day, month, holiday, road_type]])[0]

    return render_template('index.html', prediction=int(prediction))
if __name__ == '__main__':
    app.run(debug=True) 