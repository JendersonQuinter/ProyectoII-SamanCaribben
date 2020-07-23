class Client:
  def __init__(self, name, dni, age, disability, total=0, rooms=[]):
    self.name = name
    self.dni = dni
    self.age = age
    self.disability = disability
    self.total = total
    self.rooms = rooms
  
  
  def show_inf(self):
    print(f'''
    Nombre: {self.name}
    Dni: {self.dni}
    Edad: {self.age}
    Dispacidad: {self.disability}
    Habitaciones seleccionadas: {self.rooms}
    Monto total a pagar: ${self.total}
    ''')

  def inf_client(self):
    return f'''
    Nombre: {self.name}
    Dni: {self.dni}
    Edad: {self.age}
    Dispacidad: {self.disability}
    Habitaciones seleccionadas: {self.rooms}
    Monto total a pagar: ${self.total}
    '''
