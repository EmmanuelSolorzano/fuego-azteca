from odoo import http
import json
from os import getcwd
import pandas as pd
import numpy as np
import re

class MiControlador(http.Controller):
    @http.route('/fn1', type='json', auth='public', website=True)
    def fileProcessing(self, **kw):
        request_body = http.request.httprequest.data
        #print('Cuerpo de la solicitud2:', request_body)
        json_data = json.loads(request_body.decode('utf-8'))
        counter = 0
        lines = json_data['file'].split("\n")
        with open("/home/erick/odoo-custom-addons/working.csv", "w") as file:
            for line in lines:
                nCells = len(re.findall(r'",', line)) + 1
                if nCells > 3:
                    data = data[counter:]
                    file.write(data)
                    break
                counter += 1
        
            
        return f"Hola {json_data['file']} llamado por {json_data['calledBy']}!"
    

        
