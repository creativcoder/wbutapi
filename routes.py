from flask import Flask,render_template
import results

app = Flask(__name__)

@app.route('/')
def home():
	return "WBUT Api <br> Available Endpoints: <br><br> /get_results/<semno>/<roll_no> [GET]"

@app.route('/get_results/<sem>/<roll_no>')
def get_results(sem,roll_no):
    return results.fetch(sem,roll_no)

if __name__=='__main__':
	app.run(debug=True)
