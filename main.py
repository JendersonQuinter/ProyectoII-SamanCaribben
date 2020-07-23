# IMPORTS
import requests
import cruise as c
import rooms as r
import tours as t
import restaurant as rest
import statistics as s
from clases import Client


# DEFINITION FUNTIONS
def numAbundant2(num):
  parts = [f for f in range(1, num) if num % f == 0]
  plus = sum(parts)
  return plus > num

def check_prime(numb, k = 2):
  if numb % k == 0 and numb > 2:
      return False
  elif k > numb / 2:
      return True
  else:
      return check_prime(numb, k + 1)

def save_data(inf, file_name):
  with open(file_name, 'a') as f:
    f.write(f'{inf} \n')

def main():
  clients = []
  iva = 16
  api = c.api_SC()
  while True:
    try:
      welcome = int(input('''
      Bienvenido a Saman Caribbean
      ¿A qué desea ver?:

        1. Todos los Cruceros disponibles.
        2. Sistema de compra de Habitaciones.
        3. Sistema de compra de Tours.
        4. Sistema de compra de comida.
        5. Estadísticas
        6. Salir del sistema...

      > '''))
      if welcome == 1:
        c.print_cruise(api)
        back = input('Regresar (R): ').upper()
        if back == 'R':
          raise Exception
        else:
          print('Opcion invalida...')
      elif welcome == 2:
        sell_ticket = int(input('''
        Desea comprar un ticket:
        1. Por el Crucero.
        2. Por su destino.

        > '''))
        if sell_ticket == 1:
          c.print_cruise(api)
          selection = int(input('''
      Seleccione el Crucero que más le guste: '''))
          if selection:
            cruise_select = c.selection_cruise(api, selection)
            room_s = cruise_select["capacity"]["simple"]
            room_p = cruise_select["capacity"]["premium"]
            room_v = cruise_select["capacity"]["vip"]
            cost_s = cruise_select["cost"]["simple"]
            cost_p = cruise_select["cost"]["premium"]
            cost_v = cruise_select["cost"]["vip"]
            amount_people = int(input('''
      ¿Cuantas personas en total son?: '''))
            select_rooms = int(input(f'''
      ¿Qué tipo de habitacion desea comprar?
        1. Sencilla: {room_s} | {cost_s}
        2. Premium: {room_p} | {cost_p}
        3. VIP: {room_v} | {cost_v}
      
      > '''))
            if select_rooms:
              rooms_sell = []
              capacity = price = 0
              if select_rooms == 1:
                capacity = room_s
                price = cost_s
              elif select_rooms == 2:
                capacity = room_p
                price = cost_p
              elif select_rooms == 3:
                capacity = room_v
                price = cost_v

              while capacity <= amount_people:
                r.show_rooms(api, select_rooms)
                sell_room = input("Elija la habitacion que desea de   la siguiente manera (SA1): ")
                rooms_sell.append(sell_room)
                amount_people -= capacity
              neto_price = price*len(rooms_sell)
              print('''>>> PROCESO DE REGISTRO <<< ''')
              clients.append(r.register_client())
              for client in clients:
                if check_prime(client.dni):  
                  discount = 10
                elif numAbundant2(client.dni):
                  discount = 15
                if client.age > 65:
                  if select_rooms == 1:
                    print("Usted es candidato para un cambio de habitación de simple a premium")
                if client.disability == 'S':
                  discount = 30
              total_price = neto_price+(neto_price*iva/100)-(neto_price*discount/100)
              
              for client in clients:
                client.rooms = rooms_sell
                client.total = total_price
                client.show_inf()
              print(f'''
        Usted tiene un descuento del {discount}%
        Los impuestos aplicados fueron de {iva}%
        El monto neto de las habitaciones es: ${neto_price}
        ''')
              done = input("Confirmar comprar (S) o (N): ").upper()
              if done == "S":
                for client in clients:
                  save_data(client.inf_client(), "SellsRooms.txt")
              elif done == "N":
                break              
              
          else:
            raise Exception
        elif sell_ticket == 2:
          route = input("Ingrese su destino: ")
          founds = c.browser_cruise(api,route)
          c.print_cruise(api, founds)
          selection = int(input('''
          Seleccione su Crucero ideal: '''))
          if selection:
            cruise_select = c.selection_cruise(api, selection)
            room_s = cruise_select["capacity"]["simple"]
            room_p = cruise_select["capacity"]["premium"]
            room_v = cruise_select["capacity"]["vip"]
            cost_s = cruise_select["cost"]["simple"]
            cost_p = cruise_select["cost"]["premium"]
            cost_v = cruise_select["cost"]["vip"]
            amount_people = int(input('''
      ¿Cuantas personas en total son?: '''))
            select_rooms = int(input(f'''
      ¿Qué tipo de habitacion desea comprar?
        1. Sencilla: {room_s} | {cost_s}
        2. Premium: {room_p} | {cost_p}
        3. VIP: {room_v} | {cost_v}
      
      > '''))
            if select_rooms:
              rooms_sell = []
              capacity = price = 0
              if select_rooms == 1:
                capacity = room_s
                price = cost_s
              elif select_rooms == 2:
                capacity = room_p
                price = cost_p
              elif select_rooms == 3:
                capacity = room_v
                price = cost_v

              while capacity <= amount_people:
                r.show_rooms(api, select_rooms)
                sell_room = input("Elija la habitacion que desea de   la siguiente manera (SA1): ")
                rooms_sell.append(sell_room)
                amount_people -= capacity
              neto_price = price*len(rooms_sell)
              print('''>>> PROCESO DE REGISTRO <<< ''')
              clients.append(r.register_client())
              for client in clients:
                if check_prime(client.dni):  
                  discount = 10
                elif numAbundant2(client.dni):
                  discount = 15
                if client.age > 65:
                  if select_rooms == 1:
                    print("Usted es candidato para un cambio de habitación de simple a premium")
                if client.disability == 'S':
                  discount = 30
              total_price = neto_price+(neto_price*iva/100)-(neto_price*discount/100)
              
              for client in clients:
                client.rooms = rooms_sell
                client.total = total_price
                client.show_inf()
                save_data(client.inf_client(), "Compras.txt")
              print(f'''
        Usted tiene un descuento del {discount}%
        Los impuestos aplicados fueron de {iva}%
        El monto neto de las habitaciones es: ${neto_price}
        ''')
              done = input("Confirmar comprar (S) o (N): ").upper()
              if done == "S":
                for client in clients:
                  save_data(client.inf_client(), "SellsRooms.txt")
              elif done == "N":
                break
          else:
            raise Exception

      elif welcome == 3:
        dni = int(input("Ingrese su DNI: "))
        done = "S"
        while done == "S":
          people = int(input("Ingrese el número de personas que participaran en el tour: "))
          tour = int(input('''
            Tours dispinibles dentro de nuestros Cruceros:
            1. Tour en el puerto
              > $30 Por persona | Max. 4 personas por cupo.
              > Empieza a las 7:00 A.M.
              > 10 Cupos disponibles.

            2. Degustacion de comida local
              > $100 Por persona | Max. 2 personas por cupo.
              > Empieza a las 12:00 P.M.
              > 100 Cupos disponibles.

            3. Trotar por el pueblo/ciudad
              > Gratis | Sin limite de personas
              > Empieza a las 6:00 A.M
              > Sin limite de cupos
            
            4. Visita a lugares históricos
              > $40 Por persona | Max. 4 personas por cupo.
              > Empieza a las 10:00 A.M.
              > 15 Cupos disponibles.

            5. Regresar...
            
            > '''))
          if tour == 1:
            port_tour = t.port_tour(dni, people)
            print(port_tour)
            save_data(port_tour, "SellsTours.txt")
            done = input("¿Desea participar en otro Tour? (S) o (N): ").upper()
          elif tour == 2:
            taste_tour = t.taste_tour(dni, people)
            print()
            save_data(taste_tour, "SellsTours.txt")
            done = input("¿Desea participar en otro Tour? (S) o (N): ").upper()
          elif tour == 3:
            jog_tour = t.jog_tour(dni, people)
            print(jog_tour)
            save_data(jog_tour, "SellsTours.txt")
            done = input("¿Desea participar en otro Tour? (S) o (N): ").upper()
          elif tour == 4:
            visit_tour = t.visit_tour(dni, people)
            print(visit_tour)
            save_data(visit_tour, "SellsTours.txt")
            done = input("¿Desea participar en otro Tour? (S) o (N): ").upper()
          elif tour == 5:
            raise Exception
          else:
            raise Exception
      elif welcome == 4:
        pass
      elif welcome == 5:
        pass
      elif welcome == 6:
        print("Hasta luego...")
        break
      else:
        raise Exception
      break
    except:
      print("Opcion invalida...")

main()
