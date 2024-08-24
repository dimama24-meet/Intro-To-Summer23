from flask import Flask,render_template,request,redirect,url_for
from flask import session 
import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyBvX0FNq7WP6kmO0yEWLfL-BiZb8OvVWtA",
  'authDomain': "authentication-lab-267fb.firebaseapp.com",
  'projectId': "authentication-lab-267fb",
  'storageBucket': "authentication-lab-267fb.appspot.com",
 ' messagingSenderId': "582941065667",
  'appId': "1:582941065667:web:8bbe29d06394cc787bfd76",
  'databaseURL':"https://authentication-lab-267fb-default-rtdb.europe-west1.firebasedatabase.app"
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()
app=Flask(__name__, template_folder='templates',static_folder='static')

app.config['SECRET_KEY']= 'super-secret-key'

@app.route('/',methods=['GET','POST'])
def main():
  if request.method == 'POST':
    email = request.form['Email']
    password = request.form['Password']
    try:
      session['user'] = auth.create_user_with_email_and_password(email, password)
      session['quotes']=[]
      return redirect(url_for('home'))
    except Exception as e:
      print(e)

      return render_template('signup.html')
      print(e)
  else:
    return render_template('signup.html')

@app.route('/signin',methods=['GET','POST'])
def signin():
  if request.method =='POST':
    email = request.form['Email']
    password = request.form['Password']
    try:
      session['user'] = auth.sign_in_with_email_and_password(email, password)
      print('hi')
      return render_template ("home.html")
    except Exception as e:
      print(e)
      error = "authentication faild"
      print(error)
  return render_template("signin.html")

@app.route('/home',methods=['GET','POST'])
def home():
  if request.method =='POST':
    quote = request.form['quote']
    print(quote)
    session['quotes'].append(quote)
    print(session['quotes'])
    return redirect (url_for('thanks'))

  return render_template('home.html')

@app.route('/thanks',methods=['GET','POST'])
def thanks():
  return render_template('thanks.html')
@app.route('/display',methods=['GET','POST'])
def display():
  quotes = session['quotes']
  return render_template('display.html')

@app.route('/signout',methods=['GET', 'POST'])
def signout():
  pass



if __name__ == '__main__':
  app.run(debug = True)