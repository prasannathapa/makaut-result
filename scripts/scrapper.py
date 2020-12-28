import requests, sys, os, shutil
from bs4 import BeautifulSoup
from zipfile import ZipFile
import PyPDF2
import io
# user defined scripts
from . import variables

def get_result(data: dict):
    s = requests.Session()
    with s.get(variables.rooturl, headers=variables.headers) as r:
        if r.status_code != 200:
            print('check your internet connection or make sure the entered roll no range is valid')
            sys.exit(0)
        csrf_token = BeautifulSoup(r.text, 'html.parser').find('meta', {'name':'csrf-token'})['content']
    variables.data['_token'] = csrf_token
    variables.data['SEMCODE'] = variables.semcode[data['sem']]
    data1 = ""
    for rollno in range(data['start'], data['start']+data['end']):
        variables.data['ROLLNO'] = str(rollno)
        with s.post(variables.url_pdf, data=variables.data, headers=variables.headers) as r:
            pdfReader = PyPDF2.PdfFileReader(io.BytesIO(r.content))
            pageObj = pdfReader.getPage(0)
            data1 += "\n"+pageObj.extractText()
    rx = ""
    data1 += "\n1\n2\n3\n4\n"
    rx += "roll, subCode, subName, letter, cgpa, totalCredit, creditObtained\n"
    lines = data1.split("\n")
    roll = None
    marks = []
    for i in range(len(lines)):
        if(len(lines[i])>0):
            if(lines[i][0].isalpha()):
                if(lines[i][0:8] == 'ROLL NO.'):
                    if(roll != None):
                        print(roll)
                        for ix in marks:
                            rx += str(roll)+","
                            rx += ",".join(ix) + "\n"
                    marks = []
                    roll = int(lines[i+1])

                if(lines[i] == 'Points' and lines[i+1]!='Credit'):
                    while(lines[i+1][0].isupper()and i + 6 < len(lines)):
                        marks.append([lines[i+1],
                                    lines[i+2],
                                    lines[i+3],
                                    lines[i+4],
                                    lines[i+5],
                                    lines[i+6]])
                        i+=6
    if(len(marks) > 0):
        print(roll)
        for ix in marks:
            rx += str(roll)+","
            rx += ",".join(ix) + "\n"
    return rx
