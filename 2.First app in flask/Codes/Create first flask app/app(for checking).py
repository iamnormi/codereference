from flask import Flask
import views

app = Flask(__name__)

views.data()
@app.route('/')
def index():

    return "Hello World"

if __name__ == '__main__':
    pass
