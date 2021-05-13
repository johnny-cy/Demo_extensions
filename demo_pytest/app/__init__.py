from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/getName", methods=["GET"])
    def getName():
        return {"data": "this is data"}

    return app

app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
