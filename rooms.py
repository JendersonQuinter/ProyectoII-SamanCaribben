# GESTION DE HABITACIONES
from clases import Client

def register_client(rooms=[], total=0):
  while True:
    try:
      name = input("Ingrese su nombre: ")
      dni = int(input("Ingrese su DNI: "))
      age = int(input("Ingrese su edad: "))
      disability = input("Tiene alguna discapacidad (S) o (N): ").upper()
      break
    except:
      print("Error, valide sus datos...")
  client = Client(name, dni, age, disability, rooms, total)
  return client

def show_rooms(api, type_room):
  if type_room == 1:
    types = "simple"
    l = "S"
  elif type_room == 2:
    types = "premium"
    l = "P"
  elif type_room == 3:
    types = "vip"
    l = "V"
  matriz = []
  dic = {}
  hallways = api[0]['rooms'][types][0]
  rooms = api[0]['rooms'][types][1]
  j = 1
  while j <= rooms:
    matriz.append(j)
    j+=1
  print(F''' 
          >>> PISO {types.upper()} <<<
            Pasillo | Habitaciones ''')
  for letra in range(97, hallways+97):
    i = l+chr(letra).upper()
    dic[i] = matriz
    print(f'''
              {i}     | {dic[i]} 
          ''')
