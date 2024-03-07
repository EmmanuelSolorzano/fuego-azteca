from odoo import http
import json
from os import listdir
import pandas as pd
import numpy as np
import re

path = "/home/erick/odoo-custom-addons/"

def processTransactions(file):
    counter = 0
    lines = file.split("\n")
    with open("working.csv", "w") as file:
        for line in lines:
            nCells = len(re.findall(r'",', line)) + 1
            if nCells > 3:
                lines = lines[counter:]
                lines = "\n".join(lines)
                file.write(lines)
                break
            counter += 1
    
    lines = pd.read_csv("working.csv", header=0)
    
    traductionDE_ES = {
    "Datum/Uhrzeit": "Fecha/Hora",
    "Abrechnungsnummer": "Número de facturación",
    "Typ": "Tipo",
    "Bestellnummer": "Número de pedido",
    "SKU": "SKU",
    "Beschreibung": "Descripción",
    "Menge": "Cantidad",
    "Marketplace": "Mercado",
    "Versand": "envío",
    "Ort der Bestellung": "Lugar del pedido",
    "Bundesland": "Estado",
    "Postleitzahl": "Código postal",
    "Steuererhebungsmodell": "Modelo de recaudación",
    "Umsätze": "Volumen de negocios",
    "Produktumsatzsteuer": "Impuesto sobre la venta de productos",
    "Gutschrift für Versandkosten": "Crédito para gastos de envío",
    "Steuer auf Versandgutschrift": "Crédito por gastos de envío",
    "Gutschrift für Geschenkverpackung": "Crédito para envolver regalos",
    "Steuer auf Geschenkverpackungsgutschriften": "Impuesto sobre los créditos para envolver regalos",
    "Rabatte aus Werbeaktionen": "Descuentos de promociones",
    "Steuer auf Aktionsrabatte": "Impuesto sobre descuentos promocionales",
    "Einbehaltene Steuer auf Marketplace": "Impuesto retenido en el mercado",
    "Verkaufsgebühren": "Gastos de venta",
    "Gebühren zu Versand durch Amazon": "Gastos de envío de Amazon",
    "Andere Transaktionsgebühren": "Otros gastos de transacción",
    "Andere": "Otros",
    "Gesamt": "Total"}
    
    if lines.columns[0] in traductionDE_ES:
        lines.columns = lines.columns.map(traductionDE_ES)
        currency = "EUR"
    else:
        currency = "MXN"
    
    if currency == "EUR":
            lines.iloc[:, -1] = lines.iloc[:, -1].str.replace('.', '').str.replace(',', '.').astype(float)
        
    boolean_mask = lines.iloc[:, 8].isna()
    sells = lines[~boolean_mask]
    expenses = lines[boolean_mask]
    vine  = sells[sells.iloc[:, -1] < 0]
    sells = sells[sells.iloc[:, -1] > 0]
    
    checks = {"expenses": expenses, "vine": vine, "sells": sells}
    filesInDir = listdir(path)
    for key, value in checks.items():
        if f"{key}.csv" in filesInDir:
            print("Appending")
            print("Len Before", checks[key].shape)
            checks[key] = pd.concat([pd.read_csv(path+f"{key}.csv"), value])
            checks[key].to_csv(path+f"{key}.csv", index=False)
            print("Len Now", checks[key].shape)
            pd.read_csv(path+f"{key}.csv").drop_duplicates().to_csv(path+f"{key}.csv", index=False)
            print("Len After", pd.read_csv(path+f"{key}.csv").shape)
        
        else:
            print("Creating")
            checks[key].to_csv(path+f"{key}.csv", index=False)
    

def processClientesInventario(file, type):
    with open("working.csv", "w") as temp:
        temp.write(file)
    file = pd.read_csv("working.csv")
    
    if f"{type[2:]}.csv" in listdir(path):
        print("Appending")
        print("Len Before", pd.read_csv(path+f"{type[2:]}.csv").shape)
        file = pd.concat([pd.read_csv(path+f"{type[2:]}.csv"), file])
        file.to_csv(path+f"{type[2:]}.csv", index=False)
        print("Len Now", file.shape)
        pd.read_csv(path+f"{type[2:]}.csv").drop_duplicates().to_csv(path+f"{type[2:]}.csv", index=False)
        print("Len After", pd.read_csv(path+f"{type[2:]}.csv").shape)
    else:
        print("Creating")
        file.to_csv(path+f"{type[2:]}.csv", index=False)
        

class MiControlador(http.Controller):
    @http.route('/fn1', type='json', auth='public', website=True)
    def fileProcessing(self, **kw):
        request_body = http.request.httprequest.data
        json_data = json.loads(request_body.decode('utf-8'))        
        if json_data['calledBy'] == "c_amazon":
            processTransactions(json_data['file'])
            return "Archivo procesado exitosamente!"
        
        elif json_data['calledBy'] == "c_clientes":
            processClientesInventario(json_data['file'], json_data['calledBy'])
            return "Archivo procesado exitosamente!"
        
        
        elif json_data['calledBy'] == "c_inventario":
            processClientesInventario(json_data['file'], json_data['calledBy'])
            return "Archivo procesado exitosamente!"
        
            
        return f"Ocurrio un error.\n {json_data['calledBy']} no es un valor valido."
    

        
