# import os
# import datetime
# import bcrypt
# from models import *
# from flask import Flask, session, render_template, request, redirect, url_for, jsonify
# from flask_session import Session
# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker
# import logging
# from flask_sqlalchemy import SQLAlchemy
# from sendEmail import *
# from sqlalchemy import exc, or_, and_
# from ForgotEmail import *
# from OTP import *
# from flask_cors import CORS, cross_origin
# from itsdangerous import URLSafeTimedSerializer
# # from flask.ext.cors import CORS
# # from flask_cors import CORS, cross_origin
# # from itsdangerous import URLSafeTimedSerializer
# from tokens import *
# import boto3

# # ******************************
# # from itsdangerous import URLSafeTimedSerializer
# # import bcrypt
# SECRET_KEY = '9OLWxND4o83j4K4iuopO'
# SECURITY_PASSWORD_SALT = 'my_precious_two'

# def generate_confirmation_token(email):
#     serializer = URLSafeTimedSerializer(SECRET_KEY)
#     return serializer.dumps(email, salt=SECURITY_PASSWORD_SALT)


# def confirm_token(token, expiration=360000):
#     serializer = URLSafeTimedSerializer(SECRET_KEY)
#     try:
#         email = serializer.loads(
#             token,
#             salt=SECURITY_PASSWORD_SALT ,
#             max_age=expiration
#         )
#     except:
#         return False
#     return email

# # *************************