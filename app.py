from flask import Flask, render_template, send_from_directory
import json
import os

app = Flask(__name__)


@app.route('/')
def home():
    json_file_path = r'C:\Users\akaya\OneDrive - LucidMotors\Demos\vehicles.json'

    with open(json_file_path, 'r') as f:
        vehicles = json.load(f)

    # Modify the image paths to be relative to the Flask static directory
    for vehicle in vehicles:
        vehicle['images'] = [os.path.basename(img) for img in vehicle['images']]

    return render_template('index.html', vehicles=vehicles)


@app.route('/images/<filename>')
def images(filename):
    return send_from_directory(r'C:\Users\akaya\OneDrive - LucidMotors\Demos\Images', filename)


if __name__ == '__main__':
    app.run(debug=True)
