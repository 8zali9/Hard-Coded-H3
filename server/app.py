from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '<h3 style="text-align: center; border-top: 3px solid #333; border-bottom: 3px solid #333;">Hard-Coded H3</h3>'

if __name__ == "__main__":
    app.run()
