import random
from flask import Flask,render_template, request, url_for,redirect
app = Flask(__name__,
template_folder='templates',
static_folder='static')

@app.route('/home',methods=["GET","POST"])
def home():
	if request.method == 'POST':
		birth_month = request.form['birth_month']
		return redirect(url_for('fortune', birth_month=birth_month))
	else:
		return render_template('home.html')

@app.route('/fortune/<string:birth_month>')
def fortune(birth_month):
	my_fortune=["Read people mindes","Be rich for the rest of your life","Die in a car crash",
	"get back with time","you will marry your enemy","Someone you love will die",
	"A surprise will brighten your day!","Peace will surround you for the rest of your life","someone you know will kill you"]
	#len(birth_month)
	#print(my_fortune[len(birth_month)-1])
	#fortune=random.choice(my_fortune)
	if 3<= len(birth_month) <=9:
		return render_template("fortune.html", fortune=my_fortune[len(birth_month)-1])
	else:
		return render_template("home.html")
@app.route('/main', methods ='POST')
def user_name():
	user_name = request.form['user_name']


'''
@app.route('/fortune/<birth_month>')
def fortune(birth_month):
    # Example fortune based on birth month
    fortunes = {
    'January': 'You will have a productive month!',
    'February': 'Love is in the air for you!',
    'March': 'Adventure awaits you this month!',
    'April': 'Expect positive changes in your life!',
    'May': 'Your hard work will pay off soon!',
    'June': 'New opportunities are on the horizon!',
    'July': 'You will enjoy peace and relaxation!',
    'August': 'Success is coming your way!',
    'September': 'A surprise will brighten your day!',
    'October': 'You will make meaningful connections!',
    'November': 'Abundance is in your future!',
    'December': 'Joy and happiness will surround you!'}
	fortune_message = fortunes.get(birth_month, "Sorry, I don't have a fortune for that month.")
	return f"Your fortune: {fortune_message}"
'''
if __name__ == '__main__':
    app.run(debug = True)
