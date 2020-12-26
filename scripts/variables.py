csrf_token = None

semcode = {
    1: 'SM01', 2: 'SM02',
    3: 'SM03', 4: 'SM04',
    5: 'SM05', 6: 'SM06',
    7: 'SM07', 8: 'SM08'
}

folder = {
    1: 'First', 2: 'Second',
    3: 'Third', 4: 'Fourth',
    5: 'Fifth', 6: 'Sixth',
    7: 'Seventh', 8: 'Eight'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
}

rooturl = 'https://makaut1.ucanapply.com/smartexam/public/result-details'
url_pdf = 'https://makaut1.ucanapply.com/smartexam/public/download-pdf-result'

data = {
        '_token': csrf_token,
        'p1': '',
        'ROLLNO': None,
        'SEMCODE': None,
        'examtype': 'result-details',
        'all': ''
    }