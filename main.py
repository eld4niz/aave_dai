from flask import Flask, render_template
import json

app = Flask(__name__)

# Load JSON data
with open("result.json") as f:
    data = json.load(f)


# Render template
@app.route('/')
def index():
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
