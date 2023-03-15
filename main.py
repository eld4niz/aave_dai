from flask import Flask, render_template
import json
from data_extractor import defilama_api, aave_api
import threading
import time


app = Flask(__name__)


def merge_data():

    defilama_data = defilama_api()
    aave_data = aave_api()

    # combine data into a single object
    merged_data = {}
    merged_data.update(defilama_data)
    merged_data.update(aave_data)


    # convert strings to floats and round all numbers to 4 decimal places
    def round_numbers(obj):
        if isinstance(obj, str):
            try:
                return round(float(obj), 4)
            except ValueError:
                return obj
        elif isinstance(obj, float):
            return round(obj, 4)
        elif isinstance(obj, dict):
            return {k: round_numbers(v) for k, v in obj.items()}
        elif isinstance(obj, (list, tuple)):
            return [round_numbers(v) for v in obj]
        else:
            return obj


    merged_data = round_numbers(merged_data)


    # write data to file
    with open('merged_data.json', 'w') as f:
        json.dump(merged_data, f, indent=4)


def run_loop():
    while True:
        merge_data()
        time.sleep(300)  # Delay execution for 5 minutes


@app.route('/')
def index():
    
    thread = threading.Thread(target=run_loop)
    thread.start()

    # load data from JSON file
    with open('merged_data.json') as f:
        data = json.load(f)

    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
