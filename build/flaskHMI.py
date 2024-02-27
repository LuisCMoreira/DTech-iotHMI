import os
import requests
import sys

sys.path.append('./packages')

from flask import Flask, render_template, jsonify

import csvLog as Log
import jsonRead as jRead

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/config')
def config_page():
    return render_template('config.html')

@app.route('/button_click/<int:button_number>')
def button_click(button_number):
    # Call the Python function from your package
    result = Log.mainLog(jRead.getFromConfig("message.text"), f"pressed number {button_number}")
    print(button_number)
    if button_number==4:
        

        # URL of the API endpoint
        api_url = 'http://host.docker.internal:5005/dockerUpdate'

        # Make a POST request to trigger the script execution
        response = requests.post(api_url)

        # Check the response
        if response.status_code == 200:
            print('Script execution successful')
        else:
            print(f'Failed to execute script. Status code: {response.status_code}')
            print(response.text)



    # Optionally, you can return some information back to the client
    return jsonify(success=True, result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5004)
