import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View

app = Flask(__name__)
Bootstrap(app)

nav = Nav()

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")

@nav.navigation()
def navbar():
	return Navbar(
		View('Home', 'index'),
		View('About', 'about')
	)

nav.init_app(app)

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port, debug=True, use_reloader=True)