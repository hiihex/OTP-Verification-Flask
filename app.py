from flask import Flask, render_template, request, url_for, redirect, flash, session
from twilio.rest import Client, TwilioException
from flask_session import Session
from utils import generate_send_verification_code

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
app.config['SESSION_TYPE'] = 'filesystem'
ACCOUNT_SID = "twilio sid"
AUTH_TOKEN = "twilio auth token"
twilio_client = Client(ACCOUNT_SID, AUTH_TOKEN)
Session(app)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/getOTP', methods=('GET', 'POST'))
def get_otp():
    if request.method == "POST":
        if request.form['phone-number']:
            phone_number = str(request.form['phone-number'])
            try:
                code = generate_send_verification_code(twilio_client, phone_number)
            except TwilioException as e:
                return {"status":"Number is not Valid"}
            else:
                session['otp_code'] = str(code)
                return {"code":code}


@app.route('/verifyOTP', methods=('GET', 'POST'))
def verify_otp():
    if request.method == "POST":
        if request.form['verification-code']:
            code = request.form['verification-code']
            if code == session['otp_code']:
                return {"status":"success"}
            else:
                return {"status":"You entered the wrong code!"}
        else:
            return {"status":"You need to enter a code!"}


if __name__ == '__main__':
    app.run(debug=True)
