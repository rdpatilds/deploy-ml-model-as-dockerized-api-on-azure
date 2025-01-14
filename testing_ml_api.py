import json
import requests

input_data = {
  "pregnancies": 2,
  "Glucose": 100,
  "BloodPressure": 120,
  "SkinThickness": 10,
  "Insulin": 100,
  "BMI": 25,
  "DiabetesPedigreeFunction": 0.352,
  "Age": 35
}

url = "http://diabetespredictionmlapi-dev.eastus.azurecontainer.io/diabetes_prediction"
##url = "http://127.0.0.1:80/diabetes_prediction"

json_object = json.dumps(input_data)

response = requests.post(url, data=json_object)

print(response.text)
