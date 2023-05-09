from flask import Flask, request
import requests

# create the Flask app
app = Flask(__name__)
ESP32_IP = '192.168.1.100'

@app.route('/data')
def data():
    url = request.args.get('url')
    payload = {'url': url}
    r = requests.post(f'http://{ESP32_IP}/url', json=payload)
    if r.status_code == 200:
        return "URL sent successfully to ESP32"
    else:
        return "Error sending URL to ESP32"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')