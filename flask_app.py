from flask import Flask, render_template, request
from test_engine import test_sql_injection, test_xss

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test", methods=["POST"])
def run_tests():
    target_url = request.form["url"]
    sql_results = test_sql_injection(target_url)
    xss_results = test_xss(target_url)

    return render_template("results.html", sql=sql_results, xss=xss_results)

if __name__ == "__main__":
    app.run(debug=True)
