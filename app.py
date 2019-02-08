from flask import Flask, render_template, request

app = Flask(__name__)

# If not working
# windows (Run as Administrator)
    # pip install flask
# linux
    # sudo apt install python3-pip
    # pip3 install flask
# else
# In terminal
    # windows (Run as Administrator)
        # python app.py
    # linux or mac
        # python3 app.py

@app.route('/<name>', methods=["GET"])
def index(name):
    print(name)
    return render_template('index.html', name=name)

# http://localhost:2000/get?name=lol&section=b
@app.route('/get')
def get():
    name = request.args['name']
    section = request.args['section']
    return name

app.run(port=2000)
