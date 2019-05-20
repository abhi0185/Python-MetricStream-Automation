from flask import Flask,Response,send_file, render_template,request,jsonify,session,app
from Metricstream_control import *

app = Flask(__name__)

@app.route('/')
def hello():
        print("inside / hello")
        return render_template("index.html")

@app.route('/get_exception_details', methods=['POST'])
def get_exception_details():
        print("inside get_except fn in flask")
        rcvData = request.get_json()
        #from_date=request.form.get('from_date')
        #to_date=request.form.get('to_date')
        #status=request.form.get('ms_status')
        print("printing after requesting data")
        from_date=str(rcvData['field1'])
        to_date=str(rcvData['field2'])
        print(to_date)
        status=str(rcvData['field3'])
        result = Metricstream_control().get_exception_details(from_date,to_date,status)
        print(result)
        return result



if __name__ == '__main__':
        app.secret_key = 'mysecret'
        app.run(host="10.154.194.146",port=8090,debug=True,threaded=True)
