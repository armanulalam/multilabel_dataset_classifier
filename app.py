from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        input_text = request.form['description']
        output = predict_categories(input_text)[0]
        sorted_confidences = sorted(output['confidences'], key=lambda x: x['confidence'], reverse=True)
        top_classes = [elem['label'] for elem in sorted_confidences[:3]]  # Get the top 3 classes
        label_text = ", ".join(top_classes)
        return render_template("result.html", input_text=input_text, output_text=label_text)
    else:
        return render_template("index.html")

def predict_categories(input_text):
    response = requests.post("https://armanul-multilabel-dataset-classifier.hf.space/run/predict", json={
        "data": [
            input_text
        ]
    }).json()
    data = response["data"]
    return data

if __name__ == "__main__":
    app.run(debug=True)
