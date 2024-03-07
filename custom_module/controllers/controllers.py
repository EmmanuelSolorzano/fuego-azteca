from odoo import http
import json

class MiControlador(http.Controller):
    @http.route('/fn1', type='json', auth='public', website=True)
    def fileProcessing(self, **kw):
        request_body = http.request.httprequest.data
        print('Cuerpo de la solicitud2:', request_body)
        json_data = json.loads(request_body.decode('utf-8'))
        return f"Hola {json_data['file']} llamado por {json_data['calledBy']}!"
        
