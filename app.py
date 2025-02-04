from flask import Flask, request, render_template
from joblib import load

app = Flask(__name__)

# Load trained models
demand_model = load('sugar_demand_forecast_rf_model.pkl')
risk_model = load('logistic_regression_model.pkl')

# Route for home page
@app.route('/')
def home_page():
    return render_template('home.html')  

# Route for model page (if needed)
@app.route('/model')
def model_page():
    return render_template('home.html')   

# Route for demand prediction
@app.route('/predict/demand', methods=['POST'])
def predict_demand():
    # Extract data from the form
    features = [
        float(request.form['Year']),
        float(request.form['Month']),
        float(request.form['Production']),
        float(request.form['Consumption']),
        float(request.form['Imports']),
        float(request.form['Exports']),
        float(request.form['GDP']),
        float(request.form['Price']),
        float(request.form['Lag_1']),      
        float(request.form['Lag_2']),      
        float(request.form['Lag_3']) 
    ]
    # Make a prediction
    prediction = demand_model.predict([features])[0]
    # Render the result on the same page
    return render_template('home.html', demand_output=f"Predicted Demand: {prediction}")

# Route for risk prediction
@app.route('/predict/risk', methods=['POST'])
def predict_risk():
    # Extract data from the form
    features = [
        request.form['Region'],  # Encode region if necessary
        float(request.form['Crop_Yield']),
        float(request.form['Weather']),
        float(request.form['Disease_Prevalence']),
        float(request.form['Labor_Availability']),
        float(request.form['Production_Volume']),
        float(request.form['Transportation_Distance']),
        float(request.form['Fuel_Costs']),
        float(request.form['Storage_Capacity']),
        float(request.form['Domestic_Demand']),
        float(request.form['Export_Volume']),
        float(request.form['Political_Stability'])
    ]
    # Make a prediction
    prediction = risk_model.predict([features])[0]
    risk_category = 'High' if prediction == 1 else 'Low'
    # Render the result on the same page
    return render_template('home.html', risk_output=f"Predicted Risk Category: {risk_category}")

if __name__ == '__main__':
    app.run(debug=True)
