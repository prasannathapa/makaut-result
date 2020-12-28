# user defined scripts
from scripts import scrapper
from flask import Response
#python imports
import os

# flask imports
from flask import Flask, render_template, request, send_file, after_this_request
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
@app.route('/home',methods=['GET','POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = {
            'sem': int(request.form['sem']),
            'start': int(request.form['start']),
            'end': int(request.form['end'])
        }

        # script where all the scraping and zip creation is happening
        data1 = scrapper.get_result(data)

        # sends the zip file. as_attachment parameters specify that the original name of the zip will be the
        #print(data1) 
        return  Response(data1, mimetype='text/csv')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
