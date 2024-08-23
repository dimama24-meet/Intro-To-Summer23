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
  'databaseURL':""
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
app=Flask(__name__, template_folder='templates',static_folder='static')
app.config['SECRET_key']= 'super-secret-key'

@app.route('/',methods=['GET','POST'])
def main():
  if request.method == 'POST':
    email = request.form['Email']
    password = request.form['Password']
    try:
      session['user'] = auth.create_user_with_email_and_password(email, password)
      session['quotes']=[]
      return redirect(url_for('home'))
    except:
      pass
  else:
    return render_template('signup.html')

@app.route('/signin',methods=['GET','POST'])
def signin():
  if methods=='POST':
    pass


@app.route('/home',methods=['GET','POST'])
def home():
  return 1
@app.route('/thanks',methods=['GET','POST'])
def thanks():
  pass
@app.route('/display',methods=['GET','POST'])
def display():
  pass

if __name__ == '__main__':
    app.run(debug = True)