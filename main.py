from os import getenv
import json
from flask import Flask
import requests

app = Flask(__name__)
port = int(getenv("PORT", 9099))

@app.route('/')
def run_script():
	if getenv("TOUCHPOINTS_API_KEY", None) is None:
		print("Please set TOUCHPOINTS_API_KEY environment variable")
		return 'Not set up'

	api_key = environ["TOUCHPOINTS_API_KEY"]

	print(api_key)
	response = requests.get("https://api.gsa.gov/analytics/touchpoints/v1/digital_products.json?API_KEY=" + api_key)
	json_data = response.json()
	return json_data

if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=port)
