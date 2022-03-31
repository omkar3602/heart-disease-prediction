from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    form_dict = request.form.to_dict()
    print(form_dict)

    # from utils.predict import predict
    # prediction = predict(form_dict)
    prediction = 0

    return render_template("result.html", prediction=prediction)

if __name__ == "__main__":
    app.run()