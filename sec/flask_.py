

  #COMMIT
"""
from flask import Flask, render_template, request
import requests
import json
from datetime import datetime

app = Flask(__name__, template_folder='C:\\Users\\balaj\\OneDrive\\Desktop\\shortener\\sec\\templates')

@app.route('/')
def index():
    # Get parameters from the request URL
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    # Calculate the start index and end index for pagination
    start_index = (page - 1) * per_page
    end_index = start_index + per_page

    # Send a GET request to the URL
    response = requests.get('https://services.nvd.nist.gov/rest/json/cves/2.0')

    # Check if the request was successful
    if response.status_code == 200:
        # Load the JSON data
        data = json.loads(response.text)

        # Modify the date format in the data
        for vuln in data['vulnerabilities']:
            vuln['cve']['published'] = datetime.strptime(vuln['cve']['published'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d %b %Y')
            vuln['cve']['lastModified'] = datetime.strptime(vuln['cve']['lastModified'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d %b %Y')

        # Paginate the data
        paginated_data = data['vulnerabilities'][start_index:end_index]

        # Pass the data and pagination information to the HTML template
        return render_template('indexx.html', data=paginated_data, page=page, per_page=per_page)
    else:
        return f'Error: {response.status_code}'

if __name__ == '__main__':
    app.run(debug=True)
"""

"""
from flask import Flask, render_template, request
import requests
import json
from datetime import datetime

app = Flask(__name__, template_folder='C:\\Users\\balaj\\OneDrive\\Desktop\\shortener\\sec\\templates')

@app.route('/')
def index():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    start_index = (page - 1) * per_page
    end_index = start_index + per_page

    response = requests.get('https://services.nvd.nist.gov/rest/json/cves/2.0')

    if response.status_code == 200:
        data = json.loads(response.text)
        for vuln in data['vulnerabilities']:
            vuln['cve']['published'] = datetime.strptime(vuln['cve']['published'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d %b %Y')
            vuln['cve']['lastModified'] = datetime.strptime(vuln['cve']['lastModified'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d %b %Y')

        paginated_data = data['vulnerabilities'][start_index:end_index]
        total_records = len(data['vulnerabilities'])
        return render_template('indexx.html', data=paginated_data, page=page, per_page=per_page, total_records=total_records)
    else:
        return f'Error: {response.status_code}'

@app.route('/cves/<cve_id>')
def cve_detail(cve_id):
    url = f'https://services.nvd.nist.gov/rest/json/cve/2.0/{cve_id}'
    response = requests.get(url)

    # Debugging: Print the response text
    print("Response text:", response.text)

    if response.status_code == 200:
        try:
            cve_data = json.loads(response.text)
            if 'result' in cve_data and 'CVE_Items' in cve_data['result'] and cve_data['result']['CVE_Items']:
                return render_template('detail.html', cve=cve_data['result']['CVE_Items'][0])
            else:
                return 'Error: Invalid data structure'
        except json.JSONDecodeError:
            return 'Error: Failed to decode JSON response'
    else:
        return f'Error: {response.status_code}'

if __name__ == '__main__':
    app.run(debug=True)
"""

""" #SP
from flask import Flask, render_template, request
import requests
import json
from datetime import datetime

app = Flask(__name__, template_folder='C:\\Users\\balaj\\OneDrive\\Desktop\\shortener\\sec\\templates')

@app.route('/')
def index():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    start_index = (page - 1) * per_page
    end_index = start_index + per_page

    response = requests.get('https://services.nvd.nist.gov/rest/json/cves/2.0')

    if response.status_code == 200:
        data = json.loads(response.text)
        for vuln in data['vulnerabilities']:
            vuln['cve']['published'] = datetime.strptime(vuln['cve']['published'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d %b %Y')
            vuln['cve']['lastModified'] = datetime.strptime(vuln['cve']['lastModified'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d %b %Y')

        paginated_data = data['vulnerabilities'][start_index:end_index]
        total_records = len(data['vulnerabilities'])
        return render_template('indexx.html', data=paginated_data, page=page, per_page=per_page, total_records=total_records)
    else:
        return f'Error: {response.status_code}'

@app.route('/cves/<cve_id>')
def cve_detail(cve_id):
    url = f'https://services.nvd.nist.gov/rest/json/cve/2.0/{cve_id}'
    response = requests.get(url)

    if response.status_code == 200:
        try:
            cve_data = json.loads(response.text)
            if 'vulnerabilities' in cve_data and cve_data['vulnerabilities']:
                return render_template('detail.html', cve=cve_data['vulnerabilities'][0])
            else:
                return 'Error: Invalid data structure'
        except json.JSONDecodeError:
            return 'Error: Failed to decode JSON response'
    else:
        return f'Error: {response.status_code}'

if __name__ == '__main__':
    app.run(debug=True)
"""

"""SP
from flask import Flask, render_template, request
import requests
import json
from datetime import datetime

app = Flask(__name__, template_folder='C:\\Users\\balaj\\OneDrive\\Desktop\\shortener\\sec\\templates')

@app.route('/')
def index():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    start_index = (page - 1) * per_page
    end_index = start_index + per_page

    response = requests.get('https://services.nvd.nist.gov/rest/json/cves/2.0')

    if response.status_code == 200:
        data = json.loads(response.text)
        for vuln in data['vulnerabilities']:
            vuln['cve']['published'] = datetime.strptime(vuln['cve']['published'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d %b %Y')
            vuln['cve']['lastModified'] = datetime.strptime(vuln['cve']['lastModified'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d %b %Y')

        paginated_data = data['vulnerabilities'][start_index:end_index]
        total_records = len(data['vulnerabilities'])
        return render_template('indexx.html', data=paginated_data, page=page, per_page=per_page, total_records=total_records)
    else:
        return f'Error: {response.status_code}'

@app.route('/cves/<cve_id>')
def cve_detail(cve_id):
    # Fetch data from the main CVE list URL since individual CVE ID fetch is not supported
    response = requests.get('https://services.nvd.nist.gov/rest/json/cves/2.0')
    
    if response.status_code == 200:
        data = json.loads(response.text)
        for vuln in data['vulnerabilities']:
            if vuln['cve']['id'] == cve_id:
                cve_data = vuln
                return render_template('detail.html', cve=cve_data)
        return f'CVE ID {cve_id} not found'
    else:
        return f'Error: {response.status_code}'

if __name__ == '__main__':
    app.run(debug=True)


    """



from flask import Flask, render_template, request
import requests
import json
from datetime import datetime

app = Flask(__name__, template_folder='C:\\Users\\balaj\\OneDrive\\Desktop\\shortener\\sec\\templates')

@app.route('/')
def index():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    start_index = (page - 1) * per_page
    end_index = start_index + per_page

    response = requests.get('https://services.nvd.nist.gov/rest/json/cves/2.0')

    if response.status_code == 200:
        data = json.loads(response.text)
        for vuln in data['vulnerabilities']:
            vuln['cve']['published'] = datetime.strptime(vuln['cve']['published'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d %b %Y')
            vuln['cve']['lastModified'] = datetime.strptime(vuln['cve']['lastModified'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d %b %Y')

        paginated_data = data['vulnerabilities'][start_index:end_index]
        total_records = len(data['vulnerabilities'])
        return render_template('indexx.html', data=paginated_data, page=page, per_page=per_page, total_records=total_records)
    else:
        return f'Error: {response.status_code}'

@app.route('/cves/<cve_id>')
def cve_detail(cve_id):
    response = requests.get('https://services.nvd.nist.gov/rest/json/cves/2.0')
    
    if response.status_code == 200:
        data = json.loads(response.text)
        for vuln in data['vulnerabilities']:
            if vuln['cve']['id'] == cve_id:
                cve_data = vuln['cve']
                return render_template('detail.html', cve=cve_data)
        return f'CVE ID {cve_id} not found'
    else:
        return f'Error: {response.status_code}'


if __name__ == '__main__':
    app.run(debug=True)


