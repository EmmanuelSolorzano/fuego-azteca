from odoo import http
import json
from os import listdir
import pandas as pd
import numpy as np

path = "/home/erick/odoo-custom-addons/"

def getAttrs(dataset, keys):
    return {key: list(dataset[key].values) for key in keys}

class MiControlador(http.Controller):
    @http.route('/fn2', type='json', auth='public', website=True)
    def retrieve(self, **kw):
        request_body = http.request.httprequest.data
        json_data = json.loads(request_body.decode('utf-8'))
        df = pd.read_csv(path+json_data['dataset'])
        keys = json_data['keys'].split(',')
        return json.dumps(getAttrs(df, keys))