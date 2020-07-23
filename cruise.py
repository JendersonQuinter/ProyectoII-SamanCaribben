# GESTION DE CRUCEROS
import requests

def api_SC():
  url = "https://saman-caribbean.vercel.app/api/cruise-ships"

  response = requests.request("GET", url)
  return response.json()


def print_cruise(api, limit=0):
  cruise = api
  if limit != 0:
    for i in limit:
      name = cruise[i]["name"]
      route = cruise[i]["route"]
      departure = cruise[i]["departure"]
      cost_s = cruise[i]["cost"]["simple"]
      cost_p = cruise[i]["cost"]["premium"]
      cost_v = cruise[i]["cost"]["vip"]
      rooms_s = cruise[i]["rooms"]["simple"]
      rooms_p = cruise[i]["rooms"]["premium"]
      rooms_v = cruise[i]["rooms"]["vip"]
      capacity_s = cruise[i]["capacity"]["simple"]
      capacity_p = cruise[i]["capacity"]["premium"]
      capacity_v = cruise[i]["capacity"]["vip"]
      print(f'''

      {i+1}) Nombre del barco: {name}
      Ruta: {route}
      Fecha de salida: {departure}
      Precio del boleto:
        1. Sencilla: {cost_s}
        2. Premium: {cost_p}
        3. VIP: {cost_v}
      Habitaciones por piso:
        1. Sencilla: {rooms_s}
        2. Premium: {rooms_p}
        3. VIP: {rooms_v}
      Capacidad de cada habitacion:
        1. Sencilla: {capacity_s}
        2. Premium: {capacity_p}
        3. VIP: {capacity_v}
      ''')
  elif limit == 0:
    for i in range(len(cruise)):
      name = cruise[i]["name"]
      route = cruise[i]["route"]
      departure = cruise[i]["departure"]
      cost_s = cruise[i]["cost"]["simple"]
      cost_p = cruise[i]["cost"]["premium"]
      cost_v = cruise[i]["cost"]["vip"]
      rooms_s = cruise[i]["rooms"]["simple"]
      rooms_p = cruise[i]["rooms"]["premium"]
      rooms_v = cruise[i]["rooms"]["vip"]
      capacity_s = cruise[i]["capacity"]["simple"]
      capacity_p = cruise[i]["capacity"]["premium"]
      capacity_v = cruise[i]["capacity"]["vip"]
      print(f'''

      {i+1}) Nombre del barco: {name}
      Ruta: {route}
      Fecha de salida: {departure}
      Precio del boleto:
        1. Sencilla: {cost_s}
        2. Premium: {cost_p}
        3. VIP: {cost_v}
      Habitaciones por piso:
        1. Sencilla: {rooms_s}
        2. Premium: {rooms_p}
        3. VIP: {rooms_v}
      Capacidad de cada habitacion:
        1. Sencilla: {capacity_s}
        2. Premium: {capacity_p}
        3. VIP: {capacity_v}
      ''')




def browser_cruise(api, route):
  founds = []
  for i in range(len(api)):
    for j in range(len(api[i]["route"])):
      if api[i]["route"][j].upper() == route.upper():
        founds.append(i)
  if len(founds) > 0:
    return founds
  else:
    return None

def selection_cruise(api, select):
  cruise = api
  index = select - 1
  if select == 1:
    return cruise[index]
  elif select == 2:
    return cruise[index]
  elif select == 3:
    return cruise[index]
  elif select == 4:
    return cruise[index]
