from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Hello world! Version 3 ay dios help me with the webhook'

@app.route('/test')
def test():
    return 'Testing hidden functionality ;)'

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
