import os
import json
from flask import Flask
import requests

app = Flask(__name__)
port = int(os.getenv("PORT", 9099))

@app.route('/')
def run_script():
	api_key = os.getenv("TOUCHPOINTS_API_KEY", None)
	if api_key is None:
		print("Please set TOUCHPOINTS_API_KEY environment variable")
		return 'Not set up'

	print(api_key)
	response = requests.get("https://api.gsa.gov/analytics/touchpoints/v1/digital_products.json?API_KEY=" + api_key)
	json_data = response.json()
	return json_data

if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=port)
