import numpy as np
import joblib
from flask import Flask, request, jsonify , render_template

# Initialize Flask app
app = Flask(__name__,template_folder='template')

# Load the pretrained mode
model = joblib.load('model.pkl')
# Define a route to receive input from the user
@app.route('/predict', methods=['GET''POST'])
def predict():
    # Get the input data from the user
    features = request.form.values()
    print(features)

    # Convert input data into array
    input_data = [list(features)]
    input_data = np.array(input_data).astype(np.float64)
    print(input_data)

    # Make predictions using the pre-trained model
    prediction=model.predict(input_data)
    print(prediction)

    # Convert prediction to list
    output = prediction.tolist()

    # Return the prediction as a response 
    return render_template('result.html', prediction='Predicted label is {}'.format(output[0]))

   



@app.route('/')
def prediction():
# Render the result in your HTML page
    return render_template('result.html')





# Define a default route
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Start Flask app
    app.run(debug=True)