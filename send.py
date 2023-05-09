from flask import Flask
 
app = Flask(__name__)
 
@app.route('/data')
def send_data(data):
    return data
 
app.run(host='0.0.0.0', port= 8090)
