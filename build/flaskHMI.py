import sys

sys.path.append('./packages')

from flask import Flask, render_template, jsonify

import csvLog as Log
import jsonRead as jRead

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/button_click/<int:button_number>')
def button_click(button_number):
    # Call the Python function from your package
    result = Log.mainLog(jRead.getFromConfig("message.text"), f"pressed number {button_number}")

    # Optionally, you can return some information back to the client
    return jsonify(success=True, result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5004)
