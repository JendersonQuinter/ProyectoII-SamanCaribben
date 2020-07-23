# GESTION DE TOURS
def port_tour(dni, people):
  tour = "Tour en el puerto"
  participants = []
  plus = 0
  date = "7 A.M."
  price = 30*people
  limit = 4
  max_space = 10
  for i in participants:
      plus += participants[i]
      i+=1
      max_space = plus - max_space
  if max_space == 0:
      for i in participants:
          participants.pop(participants[i])
  for i in participants:
      plus += participants[i]
      i+=1
      max_space = plus - max_space 
  if people == 3:
      price = 60 + (30-30*0.1)
  elif people == 4:
      price = 60 + (30-30*0.1) + (30-30*0.1)
  if people > limit:
      return "Sobrepaso el limita maximo de personas."
  elif people <= limit and people <= max_space:
      confirmation = input(f'''
      Ha seleccionado el {tour}, el monto total será de ${price}. ¿Quiere continuar?(S) o (N): ''').upper()
      if confirmation == "S":
          return f"El Tour comienza a las {date} y el monto de su compra es ${price}." 
          participants.append(people)
      elif confirmation == "N":
          return "Hasta luego..."


def taste_tour(dni, people):
    tour = "Tour de desgustacion de comida local"
    participants = []
    plus = 0
    date = "12 P.M."
    price = 100*people
    limit = 2
    max_space = 100
    for i in participants:
        plus += participants[i]
        i+=1
        max_space = plus - max_space
    if max_space == 0:
        for i in participants:
            participants.pop(participants[i])
    for i in participants:
        plus += participants[i]
        i+=1
        max_space = plus - max_space 
    if people > limit:
        return "Sobrepaso el limita maximo de personas."
    elif people <= limit and people <= max_space:
        confirmation = input(f'''
        Ha seleccionado el {tour}, el monto total será de ${price}. ¿Quiere continuar? (S) o (N): ''').upper()
        if confirmation == "S":
            return f"El Tour comienza a las {date} y el monto de su compra es ${price}." 
            participants.append(people)
        elif confirmation == "N":
            return "Hasta luego..."


def jog_tour(dni,people):
    tour = "trotar por el parque"
    date = "6 A.M."
    confirmation = input(f'''
    Ha seleccionado el tour {tour}, el tour es gratis. ¿Desea continuar con su compra?(Si o No): ''').upper()
    if confirmation == "S":
        return f"El Tour comienza a las {date} y el monto de su compra es ${precio}."
    elif confirmation == "N":
        return "Hasta luego..."


def visit_tour(dni, people):
    participants = []
    tour = "visita a lugares historicos"
    plus = 0
    date = "10 A.M."
    price = 40*people
    limit = 4
    max_space = 15
    for i in participants:
        plus += participants[i]
        i+=1
        max_space = plus - max_space
    if max_space == 0:
        for i in participants:
            participants.pop(participants[i])
    for i in participants:
        plus += participants[i]
        i+=1
        max_space = plus - max_space 
    if people == 3:
        price = 80 + (40-40*0.1)
    elif people == 4:
        price = 80 + (40-40*0.1) + (40-40*0.1)
    if people > limit:
        return "Sobrepaso el limita maximo de personas."
    elif people <= limit and people <= max_space:
        confirmation = input(f'''
        Ha seleccionado el tour {tour}, el monto total será de ${price}. ¿Desea continuar con su compra?(S) o (N): ''').upper()
        if confirmation == "S":
            return f"El Tour comienza a las {date} y el monto de su compra es ${price}."
            participants.append(people)
        elif confirmation == "N":
            return "Hasta luego..."
