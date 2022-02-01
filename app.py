from flask import Flask, render_template, request
import itertools
from yake_keywords import yake_keywords
from split_keywords import split_keywords 

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	return render_template("index.html")

@app.route("/result", methods = ['POST','GET'])
def result():
	output = request.form.to_dict()
	job_desc = output["job_desc"]

	s_keywords = split_keywords(job_desc)
	y_keywords = yake_keywords(job_desc)

	N = 10
	s_keywords = dict(itertools.islice(s_keywords.items(), N))
	y_keywords = dict(itertools.islice(y_keywords.items(), N))

	return render_template("result.html",y_keywords = y_keywords, s_keywords = s_keywords)



if __name__ == '__main__':
	app.run(debug=True, port=5001)