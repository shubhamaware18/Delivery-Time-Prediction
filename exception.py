from flask import Flask
import sys
from DeliveryTimePrediction.logger import logging
from DeliveryTimePrediction.exception import CustomException
app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def index():
    try:
        raise Exception('We are testing our Exception file')
    
    except Exception as e:
        ML = CustomException(e, sys)
        logging.info(ML.error_message)

        logging.info('We are testing our logging file')

        return 'Welcome to our first API Home'

if __name__ == "__main__":
    app.run(debug = True)