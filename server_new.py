from flask import Flask, render_template

app = Flask(__name__)
host_addr = '0.0.0.0'
port = '8080'


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host=host_addr, port=port, debug=True)
