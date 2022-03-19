from email import contentmanager
from email.policy import default
import imp
from dump import processor, processorEngine
from sqlalchemy.orm import Session
from sqlalchemy import select


from flask import Flask, redirect,render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///processor.db'
processors = ""
try:
    # create session and add objects
    with Session(processorEngine) as session:
        statement = select(processor)
        processors = session.execute(statement).all()  
except Exception as e: print(e)
@app.route('/')
def index():
   return render_template('index.html', processors=processors)
   
    

if __name__ == "__main__":
    app.run(debug=True)