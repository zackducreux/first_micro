from flask import Flask

app = Flask(__name__)


@app.route('/name', methods=["GET"])
def hello_world():
    prefix_google = """
 <!-- Google tag (gtag.js) -->
<script async
src="https://www.googletagmanager.com/gtag/js?id=UA-250386229-1"></script>
<script>
 window.dataLayer = window.dataLayer || [];
 function gtag(){dataLayer.push(arguments);}
 gtag('js', new Date());
 gtag('config', ' UA-250386229-1');
</script>
 """
    return prefix_google + "Hello World & Zackary Ducreux"

@app.route("/")
def hello():
    app.logger.debug("A debug message")
    app.logger.info("An info message")
    app.logger.warning("A warning message")
    app.logger.error("An error message")
    app.logger.critical("A critical message")

    return "Hello, World, no error for now!"

@app.route("/info")
def info():
    app.logger.info("Hello, World!")
    return "Hello, World! (info)"

@app.route("/warning")
def warning():
    app.logger.warning("A warning message.")
    return "A warning message. (warning)"
