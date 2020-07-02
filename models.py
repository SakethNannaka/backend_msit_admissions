from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import BIGINT

db = SQLAlchemy()

class Users(db.Model) :
    __tablename__ = "Registered_users_db"
    name = db.Column(db.String, nullable = False)
    email = db.Column(db.String, primary_key=True)
    password = db.Column(db.String, nullable=False)
    knowmsit= db.Column(db.String, nullable=False)
    contact= db.Column(BIGINT(unsigned = True), nullable=False)
    education = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime(), nullable=False)
    active = db.Column(db.Boolean)

    def __init__ (self, name, email, password, knowmsit, timestamp, active, contact, education) :
        self.name = name
        self.email = email
        self.password = password
        self.knowmsit = knowmsit
        self.contact = contact
        self.education = education
        self.timestamp = timestamp
        self.active = active

class UserProfile(db.Model) :
    __tablename__ = "userProfiles"
    email = db.Column(db.String, primary_key=True)
    board_name = db.Column(db.String,nullable = False)
    board_number = db.Column(db.String,nullable = False)
    btech = db.Column(db.String,nullable = False)
    photo_status = db.Column(db.Boolean)
    full_name = db.Column(db.String,nullable = False)
    gender = db.Column(db.String,nullable = False)
    date_of_birth = db.Column(db.String,nullable = False)
    nationality = db.Column(db.String,nullable = False)
    address_line1= db.Column(db.String,nullable = False)
    address_line2= db.Column(db.String,nullable = False)
    place_town = db.Column(db.String,nullable = False)
    city = db.Column(db.String,nullable = False)
    pincode = db.Column(db.String,nullable = False)
    mobile_no = db.Column(db.String,nullable = False)
    landline_no = db.Column(db.String,nullable = False)
    parent_name = db.Column(db.String,nullable = False)
    parent_relation = db.Column(db.String,nullable = False)
    image_url = db.Column(db.String)

    def __init__ (self, email,board_name, board_number, btech, photo_status,full_name, gender, date_of_birth, nationality, address_line1, address_line2, place_town, city, pincode, mobile_no, landline_no, parent_name, parent_relation, image_url) :
        self.email = email
        self.board_name = board_name
        self.board_number = board_number
        self.btech = btech
        self.photo_status = photo_status
        self.full_name = full_name
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.nationality = nationality
        self.address_line1 = address_line1
        self.address_line2 = address_line2
        self.place_town = place_town
        self.city = city
        self.pincode = pincode
        self.mobile_no = mobile_no
        self.landline_no = landline_no
        self.parent_name = parent_name
        self.parent_relation = parent_relation
        self.image_url = image_url

class GatApplications(db.Model):
    __tablename__ = "GatApplication_db"
    email = db.Column(db.String, primary_key=True)
    gatAppNo = db.Column(db.String, nullable=True)
    testCenter = db.Column(db.String, nullable=True)
    examType = db.Column(db.String, nullable=True)
    greAnalytical = db.Column(db.String, nullable=True)
    greScore = db.Column(db.String, nullable=True)
    paymentStatus = db.Column(db.String, nullable=True)
    paymentType = db.Column(db.String, nullable=True)

    def __init__(self, email, gatAppNo, testCenter, examType, greAnalytical, greScore, paymentStatus, paymentType):
        self.email = email
        self.gatAppNo = gatAppNo
        self.testCenter = testCenter
        self.examType = examType
        self.greAnalytical = greAnalytical
        self.greScore = greScore
        self.paymentStatus = paymentStatus
        self.paymentType = paymentType


class Walkin(db.Model):
    __tablename__ = "Walkin_users_db"
    email = db.Column(db.String, primary_key=True)
    applicationNumber = db.Column(db.String, nullable=True)
    testcenter = db.Column(db.String, nullable=True)
    slotDate = db.Column(db.String, nullable=True)
    slotNo = db.Column(db.String, nullable=True)
    testTaken = db.Column(db.String, nullable=True)
    totalScore = db.Column(db.String, nullable=True)
    paymentType = db.Column(db.String, nullable=True)
    paymentStatus = db.Column(db.String, nullable=True)
    timestamp = db.Column(db.DateTime(), nullable=False)

    def __init__(self, email, applicationNumber, testcenter, slotDate, slotNo, testTaken, totalScore, paymentType, paymentStatus, timestamp):
        self.email = email
        self.applicationNumber = applicationNumber
        self.testcenter = testcenter
        self.slotDate = slotDate
        self.slotNo = slotNo
        self.testTaken = testTaken
        self.totalScore = totalScore
        self.paymentType = paymentType
        self.paymentStatus = paymentStatus
        self.timestamp = timestamp
