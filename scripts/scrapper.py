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
    for rollno in range(data['start'], data['end']+1):
        variables.data['ROLLNO'] = str(rollno)
        with s.post(variables.url_pdf, data=variables.data, headers=variables.headers) as r:
            pdfReader = PyPDF2.PdfFileReader(io.BytesIO(r.content))
            pageObj = pdfReader.getPage(0)  
            data1 += "\n"+pageObj.extractText()
    return data1 
