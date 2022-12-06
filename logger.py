from flask import Flask
import logging

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)


@app.route('/', methods=["GET"])
def main():
    # showing different logging levels
    app.logger.debug("debug log info")
    app.logger.info("Info log information")
    app.logger.warning("Warning log info")
    app.logger.error("Error log info")
    app.logger.critical("Critical log info")
    return "testing logging levels."


if __name__ == '__main__':
    app.run(debug=True)
