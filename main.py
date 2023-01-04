# import the TrendReq method from the pytrends request module
from pytrends.request import TrendReq
from flask import Flask, render_template
import sys

app = Flask(__name__)


# execute the TrendReq method by passing the host language (hl) and timezone (tz) parameters
pytrends = TrendReq(hl='en-US', tz=360)

# build list of keywords
kw_list = ["ai", "chicken", "space"]

# build the payload
pytrends.build_payload(kw_list, timeframe='2015-01-01 2015-03-31', geo='US')

# store interest over time information in df
df = pytrends.interest_over_time()

# display the top 20 rows in dataframe
print(df)


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
    print('This is error output', file=sys.stderr)
    print('This is standard output', file=sys.stdout)
    return "Hello, World, no error for now!"



@app.route("/info")
def info():
    app.logger.info(f"Hello, World! {df}")
    return f"Hello, World! \n {df}"


@app.route("/simple_chart")
def chart():
    legend = 'Monthly Data'
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    return render_template('chart.html', values=values, labels=labels, legend=legend)

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/Logger', methods=["GET"])
def logger():
    page = """
    <script> console.log('aie')</script>
    """
    return 'console' + page
