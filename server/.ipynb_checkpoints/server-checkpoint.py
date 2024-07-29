from flask import Flask, request, jsonify, render_template, send_from_directory
import util

app = Flask(__name__, template_folder='../UI')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify_image', methods=['POST'])
def classify_image():
    image_data = request.form['image_data']
    response = jsonify(util.classify_image(image_data))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
    app.run(port=5000, debug=True)