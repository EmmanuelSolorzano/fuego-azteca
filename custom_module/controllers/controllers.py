from odoo import http
import json
from os import listdir
import pandas as pd
import numpy as np
import matplotlib.colors as mcolors
from math import ceil

path = "/Users/emmanuelsolorzano/Documents/Github/odoo/addons/carga_datos/"

def getAttrs(dataset, keys):
    return {key: list(dataset[key].values) for key in keys}

def getDataEstado():
    # Function made by Emmanuel Solórzano
    df = pd.read_csv(path+"sells.csv")
    # Agrupa por el estado y suma las ventas totales
    data = df.groupby('Estado')['Cantidad'].sum().reset_index()
    # Renombra las columnas
    data.columns = ['label', 'data']
    data = {"label" : list(data['label']), "data" : list(data['data'])}
    return json.dumps(data)

def getDataProducto():
    # Function made by Kevin Barrera
    df = pd.read_csv(path+"sells.csv")
    df = df[['SKU', 'Total']]
    df = df.groupby('SKU').sum()
    df = df.sort_values(by='Total', ascending=False)
    SKU_NAMES = {
        'PT0001-1-EU': 'Elixir Ámbar',
        'PT0001-2-EU': '2-Pack Elixir Ambar',
        'PT0001-3-EU': '3-Pack Elixir Ambar',
        'PT0001-4-EU': '4-Pack Elixir Ambar',
        'PT0003-1-EU': 'Manjar Emperador',
        'PT0003-2-EU': '2-Pack Manjar Emperador',
        'PT0003-3-EU': '3-Pack Manjar Emperador',
        'PT0003-4-EU': '4-Pack Manjar Emperador',
        'PT0010-1-EU': 'Essential Pack',
        'PT0027-1-EU': 'Nutty y Picante',
        'PT0027-2-EU': '2-Pack Nutty y Picante',
        'PT0028-1-EU': 'Néctar Ígneo',
        'PT0028-2-EU': '2-Pack Néctar Ígneo'}
    df.rename(index=SKU_NAMES, inplace=True)
    return json.dumps({"label": df.index.tolist(), "data": df['Total'].tolist()})

def float_to_color(value):
    # Create a colormap that goes from red to white to green
    cmap = mcolors.LinearSegmentedColormap.from_list("my_colormap", ["#FF0000", "#FFFFFF", "#00FF00"])
    # Normalize the input value to the range [0, 1]
    normalized_value = (value + 10) / 20
    # Get the RGB color from the colormap
    rgb_color = cmap(normalized_value)
    # Convert the RGB color to a hex color
    rgb_color = "({0}, {1}, {2})".format(ceil(rgb_color[0]*255), ceil(rgb_color[1]*255), ceil(rgb_color[2]*255))
    return rgb_color

def getDataMarital():
    # Function made by Omar Alejandro Rodríguez
    df = pd.read_csv(path+"clientes.csv")
    dfMaritalStatus = df.loc[df['Demographic Type'] == 'marital_status']

    singleCustomers = dfMaritalStatus.loc[dfMaritalStatus['Demographic'] == 'Single']['Unique Customers: No. in this Demographic'].item()
    marriedCustomers = dfMaritalStatus.loc[dfMaritalStatus['Demographic'] == 'Married']['Unique Customers: No. in this Demographic'].item()

    singleCustomersColor = dfMaritalStatus.loc[dfMaritalStatus['Demographic'] == 'Single']['Unique Customers: % of Total Change in this Demographic vs Prior Period'].item()
    marriedCustomersColor = dfMaritalStatus.loc[dfMaritalStatus['Demographic'] == 'Married']['Unique Customers: % of Total Change in this Demographic vs Prior Period'].item()

    singleCustomersColorHEX = float_to_color(singleCustomersColor)
    marriedCustomersColorHEX = float_to_color(marriedCustomersColor)

    maritalStatus = {"label": ["Single", "Married"], 
                     "data": [singleCustomers, marriedCustomers],
                     "color": [singleCustomersColorHEX, marriedCustomersColorHEX]}

    return json.dumps(maritalStatus)

def getDataEdad():
    # Function made by Omar Alejandro Rodríguez
    df = pd.read_csv(path+"clientes.csv")
    dfAgeGroup = df.loc[df['Demographic Type'] == 'age_group']

    agesArray = []
    agesCount = []
    agesColor = []
    for i in dfAgeGroup.index:
        agesArray.append(dfAgeGroup['Demographic'][i])
        agesCount.append(dfAgeGroup['Unique Customers: No. in this Demographic'][i])

        agesColorHEX = float_to_color(dfAgeGroup['Unique Customers: % of Total Change in this Demographic vs Prior Period'][i])
        agesColor.append(agesColorHEX)

    for i in range(0, len(dfAgeGroup)):
        if agesArray[i] == 'Information Not Available':
            agesArray.pop(i)
            agesCount.pop(i)
            agesColor.pop(i)

    agesCount = [int(i) for i in agesCount]
    
    ageGroups = {"label": agesArray,
                    "data": agesCount,
                    "color": agesColor}
    
    return json.dumps(ageGroups)

def getDataKPI():
    # Programado por Ramiro Alejandro Ruiz
    sells = pd.read_csv(path+'sells.csv')
    vine = pd.read_csv(path+'vine.csv')
    expenses = pd.read_csv(path+'expenses.csv')
    sells.iloc[:,13] = sells.iloc[:,13].str.replace('.', '').str.replace(',', '.').astype(float)
    ### Funciones
    def sells_info(sells_total):
        data = [float(sells_total.sum().iloc[0]),float(sells_total.sum().iloc[0]/len(sells_total))]
        return data
    def vine_info(vine_total):
        data = [float(vine_total.sum().iloc[0]),float(vine_total.sum().iloc[0]/len(vine_total))]
        return data
    def expenses_info(expenses_total):
        data = [float(expenses_total.sum().iloc[0]),float(expenses_total.sum().iloc[0]/len(expenses_total))]
        return data
    ### Extracción datos
    data_sells = sells_info(sells.iloc[:,-1:])
    data_vine = vine_info(vine.iloc[:,-1:])
    data_expenses = expenses_info(expenses.iloc[:,-1:])
    ganancias_brutas = float(sells.iloc[:,13].sum())
    gastos_ventas = ganancias_brutas - data_sells[0]
    total = data_sells[0] + data_vine[0] + data_expenses[0]
    gastos_totales = data_vine[0]+data_expenses[0]-gastos_ventas

    ### Diccionario
    diccionario_datos = {"Total": total,
                        "Ganancias brutas": ganancias_brutas,
                        "Ganancias totales": data_sells[0],
                        "Ganancia promedio": data_sells[1],
                        "Gastos totales": gastos_totales,
                        "Gastos Venta": gastos_ventas
                        }
    return json.dumps(diccionario_datos)

class MiControlador(http.Controller):
    @http.route('/fn2', type='json', auth='public', website=True)
    def retrieve(self, **kw):
        request_body = http.request.httprequest.data
        json_data = json.loads(request_body.decode('utf-8'))
        key = json_data.get("data").strip().capitalize()
        print(key)
        
        if key not in ["Estado", "Producto", "Marital", "Edad", "Kpi"]:
            return json.dumps({"error": "Invalid key"})
        elif key == "Estado":
            return getDataEstado()
        elif key == "Producto":
            return getDataProducto()
        elif key == "Marital":
            return getDataMarital()
        elif key == "Edad":
            return getDataEdad()
        elif key == "Kpi":
            return getDataKPI()
