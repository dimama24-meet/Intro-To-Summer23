import random
from flask import Flask,render_template, request, url_for,redirect
app = Flask(__name__,
template_folder='templates',
static_folder='static')

@app.route('/home',methods=["GET","POST"])
def home():
	if request.method == 'GET':
		return render_template('home.html')
	else:
		return redirect(url_for('fortune',
			Birth_Month= Birth_Month,))
		name = request.form['Birth_Month']

	return render_template("home.html")

@app.route('/fortune')
def fortune():
	my_fortune=["Read people mindes","Be rich for the rest of your life","Die in a car crash",
	"get back with time"]
	fortune=random.choice(my_fortune)
	return render_template("fortune.html", fortune=fortune)


if __name__ == '__main__':
    app.run(debug = True)
