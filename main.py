from flask import Flask
ADMIN_USER = "testUser"
ADMIN_PASSWORD = "testPassword123!"
app = Flask(__name__)

class HelloWorld():

    @app.route("/")
    def index():
        return "Congratulations, it's a Python web app!"
    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=8082, debug=True)
