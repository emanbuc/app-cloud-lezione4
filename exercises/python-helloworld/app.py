from flask import Flask
from flask import json

import logging

app = Flask(__name__)

@app.route("/")
def hello():
    return "ciaone!"

@app.route('/hello')
def hello_world():
    return 'Hello World!!!'

@app.route('/status')
def status():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )

    app.logger.info("hanno chiamato status")

    return response

@app.route('/metrics')
def metrics():
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23, "jobNumber": 40}}),
            status=200,
            mimetype='application/json'
    )
    app.logger.info("richiesta metric completata con successo")
    return response
if __name__ == "__main__":
    
    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    
    app.run(host='0.0.0.0')

