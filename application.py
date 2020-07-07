import os
import datetime
import bcrypt
from models import *
from flask import Flask, session, render_template, request, redirect, url_for, jsonify
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import logging
from flask_sqlalchemy import SQLAlchemy
from sendEmail import *
from sqlalchemy import exc, or_, and_
from ForgotEmail import *
from OTP import *
from flask_cors import CORS, cross_origin
from itsdangerous import URLSafeTimedSerializer
# from flask.ext.cors import CORS
# from flask_cors import CORS, cross_origin
# from itsdangerous import URLSafeTimedSerializer
from tokens import *
import boto3
import razorpay


# ******************************
# from itsdangerous import URLSafeTimedSerializer
# import bcrypt
SECRET_KEY = '9OLWxND4o83j4K4iuopO'
SECURITY_PASSWORD_SALT = 'my_precious_two'

def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(SECRET_KEY)
    return serializer.dumps(email, salt=SECURITY_PASSWORD_SALT)


def confirm_token(token, expiration=360000):
    serializer = URLSafeTimedSerializer(SECRET_KEY)
    try:
        email = serializer.loads(
            token,
            salt=SECURITY_PASSWORD_SALT ,
            max_age=expiration
        )
    except:
        return False
    return email

# *************************

# app = Flask(_name_)   
# # Check for environment variable
# if not os.getenv("DATABASE_URL"):
#     raise RuntimeError("DATABASE_URL is not set")
# # Configure session to use filesystem
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# # db.init_app(app)
# Session(app)
# # Set up database
# engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config.from_object(__name__)
Session(app)
CORS(app, supports_credentials=True)
# CORS(app)

# s3 = S3Connection(os.environ['S3_KEY'], os.environ['S3_SECRET'])
client = boto3.client('s3')
razorpay_client = razorpay.Client(auth=("rzp_live_FGdmm48CwAcMir", "FocTLnUgxIOchp4dtwbnslay"))

@app.route("/")
@cross_origin(supports_credentials=True)
def index():
    return render_template("index.html")


@app.route("/register", methods = ["POST"])
@cross_origin(supports_credentials=True)
def register():
    data = request.get_json()
    time_stamp = datetime.datetime.now()
    salt = bcrypt.gensalt()
    password = data["password"].encode()
    password = bcrypt.hashpw(password, salt)
    reg = Users(name = data["name"], email = data["email"], password = password.decode('utf-8'), knowmsit = data["selectValue"], contact= int(data["contact"]), education = data["education"], timestamp = time_stamp , active = False)

    try:
        db.session.add(reg)
        db.session.commit()
        send_email(data["email"],generate_confirmation_token(data["email"]))
        return ({"statuscode":200, "success": "user registered successfully"})
    except exc.IntegrityError:
        return ({"statuscode": 400, "Error":"User already exists" })
    except:
        print('exception message', 'something went wrong while adding user')
        return ({"statuscode": 500, "Error":"something went wrong while sending email" })

@app.route("/changepassword", methods = ["POST"])
@cross_origin(supports_credentials=True)
def changePassword():
    # try:
    data = request.get_json()
    print(data)
    # email = session["email"] This needs to be used when it is integrated with front end
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(session.get("email"))
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    email = data['email']
    # email = session['email']
    # print(email)
    salt = bcrypt.gensalt()
    pwd = data["password"].encode()
    pwd = bcrypt.hashpw(pwd, salt)
    userobj = Users.query.get(email)
    userobj.password = pwd.decode('utf-8')
    db.session.add(userobj)
    db.session.commit()
    return ({"success": True, "statuscode": 200, "message" : "sucessfully updated password"})
    # except:
    #     return ({"message" : "Something went wrong in updating the password"})
@app.route("/login", methods = ["POST"])
@cross_origin(supports_credentials=True)
def login():
    try:
        data = request.get_json()
        print(data)
        email = data["email"]
        pwd = data["password"]
        pwd = pwd.encode('utf-8')
        userobj = Users.query.get(email)
        if userobj:
            print(userobj.active)
            if (bcrypt.checkpw(pwd, userobj.password.encode('utf-8'))):
                if (userobj.active):
                    
                    session['email'] = email
                    session.permanent = True
                    return ({"auth": True, "message": "You have successfully logged in"})
                else:
                    return ({"auth": False, "message": "Please click the activation link we sent to your email."})
            else:
                return {"auth": False, "message": "Please enter correct password"}
        else:
            return ({"auth": False, "message":"User not exists. Please register to login" })
    except:
        return ({"auth": False, "message":"Internal server error" })

            
@app.route('/logout',methods=['POST'])
@cross_origin(supports_credentials=True)
def logout():
    print("session cleared")
    session.clear()
    return({"auth": False, "message":"You have  logged out successfully "})
        

@app.route('/session',methods=['get'])
@cross_origin(supports_credentials=True)
def check_session():
    print('entered')
    print(session.get('email'))
    if(session.get('email')):
        print(True)
        userobj=Users.query.get(session.get("email"))
        return ({"statuscode":200, "success": True,'active':userobj.active})
    else:
        return ({"statuscode":400, "error": False})

@app.route('/forgot', methods=["POST"])
@cross_origin(supports_credentials=True)
def forgot():
    data = request.get_json()
    email = data.get('email')
    if not email:
        return ({"statuscode": 400, "error": "SchemaValidationError"})
    user = Users.query.get(email)
    if not user:
        return ({"statuscode": 401, "error": "EmailDoesnotExistsError"})
    print(user.timestamp)
    otp = generateOTP()
    session['otp'] = str(otp)
    forgot_email(email, otp)
    return ({"statuscode": 200, "success": "OTP Sent sucessfully", "otp": str(otp)})

@app.route('/send',methods=["POST"])
@cross_origin(supports_credentials=True)
def recieve():
    data = request.get_json()
    print(session.get('otp')==data['otp'])
    if (session.get('otp')==data['otp']):
        return ({"statuscode":200,"success":"OTP Verified sucessfully"})
    else:
        return ({"statuscode":400,"error":"OTP Verification failed"})
        

@app.route('/reset',methods=["POST"])
@cross_origin(supports_credentials=True)
def reset():
    try:
        salt = bcrypt.gensalt()
        data = request.get_json()
        email = data['email']
        # password  = data['password']
        pwd = data["password"].encode()
        pwd = bcrypt.hashpw(pwd, salt)
        userobj = Users.query.get(email)
        userobj.password = pwd.decode('utf-8')
        db.session.add(userobj)
        db.session.commit()
        return ({"success": True, "status code": 200, "message" : "sucessfully updated password"})
    except:
        return ({"message" : "Something went wrong in updating the password"})

@app.route('/confirm_email/<token>')
@app.route('/confirm_email/',methods=["GET,POST"])
@cross_origin(supports_credentials=True)
def confirm_email(token):
    try:
        email = confirm_token(token)
        print(f"____******{email}")
    except:
        print('The confirmation link is invalid or has expired,danger')
        return('The confirmation link is invalid or has expired,danger')
    user = Users.query.filter_by(email=email).first()
    if user.active:
        print('Account already confirmed. Please login ,success')
        return('Account already confirmed. Please login ,success')
    else:
        user.active = True
        db.session.add(user)
        db.session.commit()
        print('You have confirmed your account. Thanks!,success')
        return('You have confirmed your account. Thanks!,success')

@app.route('/profile', methods = ["POST"])
@cross_origin(supports_credentials=True)
def profile():
    data = request.get_json()
    # print(data["postData"])
    data = data["postData"]
    print(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>{data}<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    if (len(data["board_name"]) >1 and len(data["board_number"]) >1 and len(data["pincode"]) >1 and len(data["address_line1"]) >1 and len(data["image_url"]) >1 and len(data["mobile_no"])>1 ):
        print(True)
        data["photo_status"]=True
    else:
        data["photo_status"]=False
    profile = UserProfile(email = data["email"], board_name = data["board_name"], board_number = data["board_number"], btech = data["btech"], photo_status =data["photo_status"] ,full_name = data["full_name"], gender = data["gender"], date_of_birth = data["date_of_birth"], nationality = data["nationality"], address_line1 = data["address_line1"], address_line2 = data["address_line2"], place_town = data["place_town"], city = data["city"], pincode = data["pincode"], mobile_no = data["mobile_no"], landline_no = data["landline_no"], parent_name = data["parent_name"], parent_relation = data["parent_relation"], image_url = data["image_url"])
    try:
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>entered Try<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        db.session.add(profile)
        db.session.commit()
        return ({"statuscode":200, "success": "profile updated successfully"})
    except exc.IntegrityError:
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>entered IntegrityError<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        db.session.rollback()
        email = data["email"]
        user  = UserProfile.query.get(email)
        print(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>{user}<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        user.full_name = data["full_name"]
        user.parent_name = data["parent_name"]
        user.parent_relation = data["parent_relation"]
        user.date_of_birth=data["date_of_birth"]
        user.board_number=data["board_number"]
        user.btech=data["btech"]
        user.photo_status=data["photo_status"]
        user.gender=data["gender"]
        user.address_line1=data["address_line1"]        
        user.nationality=data["nationality"]
        user.address_line2=data["address_line2"]
        user.place_town=data["place_town"]
        user.pincode=data["pincode"]
        user.city=data["city"]
        user.mobile_no=data["mobile_no"]
        user.landline_no=data["landline_no"]
        user.board_name=data["board_name"]
        db.session.commit()
        return ({"statuscode": 201, "success":"profile modified successfully" })
    except:
        print("entered")
        return ({"statuscode": 500, "Error":"something went wrong adding profile"})


@app.route("/image", methods = ["POST"])
@cross_origin(supports_credentials=True)
def image():
    file = request.files['file']
    response = client.put_object(
    Body= file,
    Bucket='admissionsimagebucket',
    Key= file.filename,
    )
    print(response)
    return ({'response':response, 'message' : "successfully updated"})
    
# flask_cors.CORS(app, expose_headers='Authorization')

@app.route("/gatApplication", methods=["POST"])
def gatApplication():
    data = request.get_json()
    email = data["email"]
    userobj = GatApplications.query.get(email)
    num = GatApplications.query.count()
    # print("appNo ", appNo)
    if not userobj:
        appNo = "202G" + str(f'{(num+1):05}')
        return ({"statuscode": 200, "appNo": appNo, "applied": False})
    else:
        gatDetails = {"appNo": userobj.gatAppNo, "testCenter": userobj.testCenter,
                      "paymentStatus": userobj.paymentStatus, "examType": userobj.examType, "greAnalytical": userobj.greAnalytical, "greScore": userobj.greScore}
        return ({"statuscode": 200, "applied": True, "gatDetails": gatDetails})


@app.route("/gatDetails", methods=["POST"])
def GATdetails():
    data = request.get_json()
    email = data["email"]
    print(email, data['applicationNo'], data['testCenter'], data["appType"])
    userobj = GatApplications.query.get(email)
    print(userobj)
    try:
        if userobj:
            userobj.testCenter = data['testCenter']
            userobj.examType = data["appType"]
            userobj.greAnalytical = data["analytical"]
            userobj.greScore = data["quantVerbal"]
            db.session.commit()
            return ({"statuscode": 200, "status": "updated", "payment": userobj.paymentStatus})
        gatApplication = GatApplications(email=email, gatAppNo=data['applicationNo'], testCenter=data['testCenter'], examType=data["appType"],
                                         greAnalytical=data["analytical"], greScore=data["quantVerbal"], paymentStatus="pending", paymentType=None)
        db.session.add(gatApplication)
        db.session.commit()
        return ({"statuscode": 200, "status": "inserted", "payment": "pending"})
    except exc.IntegrityError:
        return ({"statuscode": 400, "status": "Integration error"})
    except:
        return ({"statuscode": 500, "status": "something went wrong while updating"})

    #     return ({"statuscode": 400, "status": "updation failed"})
    # except:
    #     return ({"statuscode": 500, "status": "something went wrong while updating"})


@app.route("/walkin", methods=["POST"])
def walkinApplication():
    data = request.get_json()
    email = data["email"]
    userobj = Walkin.query.get(email)
    num = Walkin.query.count()
    # print("appNo ", appNo)
    if not userobj:
        print("email", email)
        appNo = "202W" + str(f'{(num+1):05}')
        return ({"statuscode": 200, "appNo": appNo, "applied": False})
    else:
        walkinDetails = {"appNo": userobj.applicationNumber, "testCenter": userobj.testcenter,
                         "paymentStatus": userobj.paymentStatus, "slotDate": userobj.slotDate, "totalScore": userobj.totalScore}
        return ({"statuscode": 200, "applied": True, "walkinDetails": walkinDetails})


@app.route("/walkinDetails", methods=["POST"])
def WalkinDetails():
    data = request.get_json()
    email = data["email"]
    timestamp = datetime.datetime.now()

    try:
        walkinApplication = Walkin(email=email, applicationNumber=data['applicationNo'], testcenter=data['testCenter'],
                                   totalScore="Exam not taken", slotDate="pending", slotNo="pending", testTaken="pending", paymentStatus="pending", paymentType=None, timestamp=timestamp)
        db.session.add(walkinApplication)
        db.session.commit()
        return ({"statuscode": 200, "status": "updated", "totalScore": "Exam not taken", "slotDate": "pending", "paymentStatus": "pending"})
    except exc.IntegrityError:
        return ({"statuscode": 400, "status": "failed"})
    except:
        return ({"statuscode": 500, "status": "something went wrong while updating"})

@app.route("/getProfile",methods=["POST"])
@cross_origin(supports_credentials=True)
def getProfile():
    data = request.get_json()
    print(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>{data}<<<<<<<<<<<<<<<<<<<")
    email=data["email"]
    print(f"<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<{email}>>>>>>>>>>>>>>>>>>>")
    userObj  = UserProfile.query.get(email)
    if userObj:
        print(True)
        userprofile = {
        "full_name":userObj.full_name,
        "parent_name":userObj.parent_name,
        "gender":userObj.gender,
        "address_line1":userObj.address_line1,
        "address_line2":userObj.address_line2,
        "city":userObj.city,
        "place_town":userObj.place_town,
        "pincode":userObj.pincode,
        "mobile_no":userObj.mobile_no,
        "landline_no":userObj.landline_no,
        "board_number":userObj.board_number,
        "board_name":userObj.board_name,
        "btech":userObj.btech,
        "image_url":userObj.image_url,
        "email":userObj.email,
        "date_of_birth":userObj.date_of_birth,
        "parent_relation":userObj.parent_relation,
        "nationality":userObj.nationality,
        "photo_status":userObj.photo_status,

        }


        return ({'response':userprofile, 'message' : "True"})
    else:
        return ({'response':userObj, 'message' : "False"})

@app.route("/orders", methods=["GET", "POST"])
def order():
    amount = 1000
    currency = "INR"
    payment_capture = 1
    payment = razorpay_client.order.create(amount= amount, currency= currency, payment_capture= payment_capture)
    return payment