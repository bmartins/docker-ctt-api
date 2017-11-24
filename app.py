import datetime
import json
from bottle import Bottle , abort, route, run, response, request
from ctt import get_package_status


app = application = Bottle()

@app.route('/ctt/packagestatus/<p_id>', method='GET')
def search(p_id):

    status = get_package_status(p_id)
    return status

@app.route('/ctt/status', method='GET')
def status():
    return {"ok": 1}

#app.run(host='0.0.0.0', port=8001, debug=True)
