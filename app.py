from fileinput import filename
import process
#from process import main

from flask import Flask, render_template, request

app = Flask(__name__)

# routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")

@app.route("/about")
def about_page():
	return "About page"

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		vid = request.files['my_video']

		vid_path = "static/" + vid.filename	
		vid.save(vid_path)

		text = process.main(vid_path)

	return render_template("index.html", prediction = text, vid_path = vid_path)


if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)


#main("sample-video.mp4")