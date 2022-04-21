from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return "hello world!"

host_addr = "0.0.0.0"
port_num = "8080"

if __name__ == "__main__":
    app.run(host=host_addr, port=port_num, debug=True)
