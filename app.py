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


@app.route('/')
def index():
    try:
        # create session and add objects
        with Session(processorEngine) as session:
            statement = select(processor)
            processors = session.execute(statement).all()  
            for row in processors:
                print(row.processorName)
            return render_template('index.html', processors=processors)
    except Exception as e: print(e)
    return "Somthing wrong!"
    

if __name__ == "__main__":
    app.run(debug=True)