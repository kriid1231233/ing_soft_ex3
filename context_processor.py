import requests
import json

def total_carrito(request):
    total = 0
    if request.user in request. session:
        try:
            for key, value in request.session['carrito'].items():
                total = total + (int(value['precio']))*(value['cantidad'])
        except:
            request.session['carrito']={}
            total = 0
    return {'total_carrito':int(total)}



def dolar_hoy(request):
    url = 'https://mindicador.cl/api/dolar'
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        documento = json.loads(respuesta.text)
        dolar_hoy_valor = documento['serie'][0]['valor']
        return {'dolar_hoy': dolar_hoy_valor}
    else:
        return {'dolar_hoy': None}