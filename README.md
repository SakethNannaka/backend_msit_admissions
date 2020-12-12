# msit-admissions

MSIT admissions is a web programme that is used to apply for the MSIT entrance exam. This is the back-end portion of MSIT admissions.Developed with Flask/Python and Deployed on Heroku

Project Flow:

The main module of this project is application.py,Locally we launch the programme by running the flask and setting the path to the module application py. But since it is being deployed on Heroku , we have to mention what to start using procfile .


Here in the procfile we start the module wsgi.py using gunicorn. wsgi.py imports all the modules from application.py.



ProcFile(started by heroku)-> wsgi.py(started by procFile using gunicorn)-> application.py(imported in wsgi.py).

 Modules Like :
  sendEmail.py 
  ForgotEmail.py
  OTP.py
  test_Files.py
  Email_helper.py
which are used as seperate modules to reduce the complexity and ease of use of application.py

other modules :
    models.py
    create.py 
are used to declare and create tables in the database

Other credentials related to database and boto3[AWS] are declared as configVars on heroku
