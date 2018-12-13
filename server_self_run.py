from flask import Flask, request, jsonify
import json
import requests

app = Flask(__name__)
port = '5000'

@app.route('/', methods=['GET'])
def index():
  # FETCH THE View Name
  view_name = 'Software Change'
  # FETCH job details
  getURL = r"https://spc-jenkins.mo.sap.corp/view/"+view_name+"/api/json?tree=jobs[name]"
  print(getURL)
  r = requests.get(getURL)
  #http://mo-4fa780a4e:8080/view/Software%20Change/api/json?pretty=true&tree=jobs[name,color] jijo
  return jsonify(
    status=r.status_code,
    replies=[{
        'type': 'text',
        'content': r.json()['jobs']
    }]
  )



@app.route('/errors', methods=['POST'])
def errors():
  print(json.loads(request.get_data()))
  return jsonify(status=200)

app.run(port=port)