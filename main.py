from flask import Flask, render_template
from second import second

app = Flask(__name__)
app.register_blueprint(second,url_prefix="/admin")

@app.route("/home")
@app.route("/")
def test():
    return "<h2>test</h2>"

if __name__ == "__main__":
    app.run(debug=True)
