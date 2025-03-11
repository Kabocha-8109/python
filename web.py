from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello 曾俊諭!"
@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"


if __name__ == "__main__":
    app.run()
