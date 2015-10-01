from flask import Flask,render_template
import results

app = Flask(__name__)

@app.route('/')
def home():
	return "WBUT Api <br> Available Endpoints: <br><br> /get_results [GET]"

@app.route('/get_results')
def get_results():
	return "HELP: Pass in semester no and roll no as query params"

if __name__=='__main__':
	app.run(debug=True)
