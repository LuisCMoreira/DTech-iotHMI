from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/dockerUpdate', methods=['POST'])
def run_script():
    subprocess.run(['.\dockerUpdate.bat'])
    return 'Script executed successfully'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
