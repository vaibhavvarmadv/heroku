from flask import Flask, render_template, request
from flasgger import Swagger

#WSGI - it is an intermediate server between backend and frontend
app = Flask(__name__)
Swagger(app)

@app.route('/', methods = ['GET', 'Post'])
def welcome():
    return render_template('index.html')

@app.route('/name/<your_name>')
def names(your_name):
    return f"Welcome to Praxis {your_name}"

@app.route('/checking_route')
def req_params():
    name = request.args.get("Student_Name")

    roll_no = request.args.get("roll_no")

    return f"Student name is {name} and roll number is {roll_no}", 206

# Defining using Swagger
@app.route('/checking_req',methods=['POST','GET'])
def get_req_parameters():
    """ Practicing Swagger
    ---
    parameters:
     - name: Student_name
       in: query
       type: string
       required: true
     - name: roll_no
       in: query
       type: number
       required: true
    responses:
       200:
            description: Result is

    """
    name = request.args.get("Student_name")
    roll_no = request.args.get("roll_no")
    return f"Student name is {name} and roll no is {roll_no} in Praxis"

    

if __name__ == '__main__':

    app.run(debug = True, host = '0.0.0.0', port = 3400)