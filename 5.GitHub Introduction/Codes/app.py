from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html', title = "Flask App")


if __name__ == '__main__':
    app.run(debug = True)
