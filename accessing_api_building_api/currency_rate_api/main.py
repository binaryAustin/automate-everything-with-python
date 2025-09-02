from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Currency rate API</h1><p>Example URL: /api/v1/usd-eur</p>"


@app.route("/api/v1/<in_cur>-<out_cur>")
def convert(in_cur: str, out_cur: str):
    pass


app.run()
