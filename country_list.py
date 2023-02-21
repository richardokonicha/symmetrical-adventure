from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    countries = ["Nigeria", "Tunisia", "Gabon", "Cameroon", "China", "USA", "UK", "Portugal", "Bali"]
    return render_template('./dashboard.html', countries=countries)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)