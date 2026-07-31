from flask import Flask

app = Flask(__name__)

@app.route("/orders")
def orders():

    return {
        "service": "Order Service"
    }

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5003
    )
