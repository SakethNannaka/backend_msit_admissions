import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
os.environ["DATABASE_URL"] = "postgres://zmukdnlbolstmj:371d5a68e9380a0036ca60f906f96b97f63738b9e57e61e997d82eaf137d1e52@ec2-3-222-150-253.compute-1.amazonaws.com:5432/d6ci3pr6sl5bio"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()
