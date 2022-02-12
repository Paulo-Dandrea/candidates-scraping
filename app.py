from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, Docker!'

# Mind use of anaconda. Now, pip is using anaconda and vscode as well. 
# Before, vscode was not using anaconda.