Ejercico 2
class Fecha:
  def _init_(self, dia=none, mes=none, año=none):
    if dia is None or mes is None or año is None:
      hoy=datetime.today()
      self.dia= hoy.day
      self.mes= hoy.month
      self.año= hoy.year
    else:
      self.dia= dia
      self.mes= mes
      self.año= año
 def __str__(self):
      return f"{self.dia:08d}/{self.mes:07}/{self.año}"
 def __eq__(self, otra_fecha):
      return (self.dia= otra_fecha.dia and
       self.mes= otra_fecha.mes and
       self.año= otra_fecha.año)
 def calcular_dif_fecha(self, otra_fecha):
      fecha1 = datetime(self.año, self.mes, self.dia)
      fecha2 = datetime(otra_fecha.año, otra_fecha.mes, otra_fecha.dia)
      diferencia = abs((fecha1-fecha2).days)
     return diferencia

class Alumno(dict):
  def __init__(self, nombre, dni, fecha_ingreso, carrera):
    super().__init__(Nombre=nombre, DNI=dni, FechaIngreso=fecha_ingreso, Carrera=carrera)
     self['Nombre'] = nombre
     self['DNI'] = dni
     self['FechaIngreso'] = fecha_ingreso
     self['Carrera'] = carrera
  def __str__(self):
    return (f"Nombre: {self['Nombre']}, DNI: {self['DNI']},
    f"Fecha de Ingreso: {self['FechaIngreso']}, Carrera: {self['Carrera']}")
  def __eq__(self, otro_alumno):
    return self['DNI'] == otro_alumno['DNI']
  def actualizar_datos(self, nombre=None, dni=None, fecha_ingreso=None, carrera=None):
    if nombre is not None:
    self['Nombre'] = nombre
    if dni is not None:
    self['DNI'] = dni
    if fecha_ingreso is not None:
    self['FechaIngreso'] = fecha_ingreso
    if carrera is not None:
    self['Carrera'] = carrera
 def antiguedad(self):
    fecha_ingreso = datetime(self['FechaIngreso'].año, self['FechaIngreso'].mes, self['FechaIngreso'].dia)
    hoy = datetime.today()
    diferencia = hoy - fecha_ingreso
    return diferencia.days


ejercico 3

class Fecha:
  def __init__(self, dia=None, mes=None, año=None):
   if dia is None or mes is None or año is None:
      hoy = datetime.today()
      self.dia= hoy.day
      self.mes= hoy.month
      self.año= hoy.year
   else:
      self.dia= dia
      self.mes= mes
      self.año= año
  def __str__(self):
    return f"{self.dia:02}/{self.mes:02}/{self.año}"
  def __eq__(self, otra_fecha):
    return (self.dia == otra_fecha.dia and
            self.mes == otra_fecha.mes and
            self.año == otra_fecha.año)
  def calcular_dif_fecha(self, otra_fecha):
    fecha1 = datetime(self.año, self.mes, self.dia)
    fecha2 = datetime(otra_fecha.año, otra_fecha.mes, otra_fecha.dia)
    diferencia = abs((fecha1-fecha2).days)
    return diferencia
    
class Alumno(dict):
  def __init__(self, nombre, dni, fecha_ingreso, carrera):
    super().__init__(Nombre=nombre, DNI=dni, FechaIngreso=fecha_ingreso, Carrera=carrera)
      self['Nombre'] = nombre
      self['DNI'] = dni
      self['FechaIngreso'] = fecha_ingreso
      self['Carrera'] = carrera
  def __str__(self):
     return (f"Nombre: {self['Nombre']}, DNI: {self['DNI']}, "
             f"Fecha de Ingreso: {self['FechaIngreso']}, Carrera: {self['Carrera']}")
  def __eq__(self, otro_alumno):
     return self['DNI'] == otro_alumno['DNI']
  def actualizar_datos(self, nombre=None, dni=None, fecha_ingreso=None, carrera=None):
     if nombre is not None:
        self['Nombre'] = nombre
     if dni is not None:
        self['DNI'] = dni
     if fecha_ingreso is not None:
        self['FechaIngreso'] = fecha_ingreso
     if carrera is not None:
        self['Carrera'] = carrera

 def antiguedad(self):
     fecha_ingreso = datetime(self['FechaIngreso'].anio, self['FechaIngreso'].mes, self['FechaIngreso'].dia)
     hoy = datetime.today()
     diferencia = hoy - fecha_ingreso
     return diferencia.days

class Nodo:
   def __init__(self, dato=None):
      self.dato = dato
      self.siguiente = None
      self.anterior = None

class ListaDoblementeEnlazada:
   def __init__(self):
      self.cabeza = None
      self.cola = None
   def append(self, dato):
      nuevo_nodo = Nodo(dato)
    if self.cabeza is None:
       self.cabeza = nuevo_nodo
       self.cola = nuevo_nodo
    else:
       self.cola.siguiente = nuevo_nodo
       nuevo_nodo.anterior = self.cola
       self.cola = nuevo_nodo
  def __iter__(self):
        self.actual = self.cabeza
        return self
  def __next__(self):
      if self.actual is None:
          raise StopIteration
      else:
          dato = self.actual.dato
          self.actual = self.actual.siguiente
          return dato
  def lista_ejemplo(self, cantidad=5):
        nombres = ['Maria', 'David', 'Carolina', 'Maria jose', 'Cynthia', 'Leonardo', 'Tomas', 'Francisco', 'Fatima', 'Victor']
        carreras = ['Odontologia', 'Programacion', 'Medicina', 'ProfesoradodeBiologia', 'Arte']
        for _ in range(cantidad):
           nombre = random.choice(nombres)
           dni = random.randint(10000000, 99999999)
           dia = random.randint(1, 28)
           mes = random.randint(1, 12)
           año = random.randint(2010, 2022)
           fecha_ingreso = Fecha(dia, mes, año)
           carrera = random.choice(carreras)
           alumno = Alumno(nombre, dni, fecha_ingreso, carrera)


ejercicio 4

class Fecha:
  def __init__(self, dia=None, mes=None, año=None):
   if dia is None or mes is None or año is None:
      hoy = datetime.today()
      self.dia= hoy.day
      self.mes= hoy.month
      self.año= hoy.year
   else:
      self.dia= dia
      self.mes= mes
      self.año= año
  def __str__(self):
    return f"{self.dia:02}/{self.mes:02}/{self.año}"
  def __eq__(self, otra_fecha):
    return (self.dia == otra_fecha.dia and
            self.mes == otra_fecha.mes and
            self.año == otra_fecha.año)
  def calcular_dif_fecha(self, otra_fecha):
    fecha1 = datetime(self.año, self.mes, self.dia)
    fecha2 = datetime(otra_fecha.año, otra_fecha.mes, otra_fecha.dia)
    diferencia = abs((fecha1-fecha2).days)
    return diferencia
    
class Alumno(dict):
  def __init__(self, nombre, dni, fecha_ingreso, carrera):
    super().__init__(Nombre=nombre, DNI=dni, FechaIngreso=fecha_ingreso, Carrera=carrera)
      self['Nombre'] = nombre
      self['DNI'] = dni
      self['FechaIngreso'] = fecha_ingreso
      self['Carrera'] = carrera
  def __str__(self):
     return (f"Nombre: {self['Nombre']}, DNI: {self['DNI']}, "
             f"Fecha de Ingreso: {self['FechaIngreso']}, Carrera: {self['Carrera']}")
  def __eq__(self, otro_alumno):
     return self['DNI'] == otro_alumno['DNI']
  def actualizar_datos(self, nombre=None, dni=None, fecha_ingreso=None, carrera=None):
     if nombre is not None:
        self['Nombre'] = nombre
     if dni is not None:
        self['DNI'] = dni
     if fecha_ingreso is not None:
        self['FechaIngreso'] = fecha_ingreso
     if carrera is not None:
        self['Carrera'] = carrera

 def antiguedad(self):
     fecha_ingreso = datetime(self['FechaIngreso'].anio, self['FechaIngreso'].mes, self['FechaIngreso'].dia)
     hoy = datetime.today()
     diferencia = hoy - fecha_ingreso
     return diferencia.days

class Nodo:
   def __init__(self, dato=None):
      self.dato = dato
      self.siguiente = None
      self.anterior = None

class ListaDoblementeEnlazada:
   def __init__(self):
      self.cabeza = None
      self.cola = None
   def append(self, dato):
      nuevo_nodo = Nodo(dato)
    if self.cabeza is None:
       self.cabeza = nuevo_nodo
       self.cola = nuevo_nodo
    else:
       self.cola.siguiente = nuevo_nodo
       nuevo_nodo.anterior = self.cola
       self.cola = nuevo_nodo
  def __iter__(self):
        self.actual = self.cabeza
        return self
  def __next__(self):
      if self.actual is None:
          raise StopIteration
      else:
          dato = self.actual.dato
          self.actual = self.actual.siguiente
          return dato
  def lista_ejemplo(self, cantidad=5):
        nombres = ['Maria', 'David', 'Carolina', 'Maria jose', 'Cynthia', 'Leonardo', 'Tomas', 'Francisco', 'Fatima', 'Victor']
        carreras = ['Odontologia', 'Programacion', 'Medicina', 'ProfesoradodeBiologia', 'Arte']
        for _ in range(cantidad):
           nombre = random.choice(nombres)
           dni = random.randint(10000000, 99999999)
           dia = random.randint(1, 28)
           mes = random.randint(1, 12)
           año = random.randint(2010, 2022)
           fecha_ingreso = Fecha(dia, mes, año)
           carrera = random.choice(carreras)
           alumno = Alumno(nombre, dni, fecha_ingreso, carrera)
           return self

    def ordenar_por_fecha_ingreso(self):
        if self.cabeza is None:
            return
        cambiado = True
        while cambiado:
            cambiado = False
            actual = self.cabeza
            while actual.siguiente is not None:
                if actual.dato['FechaIngreso'] > actual.siguiente.dato['FechaIngreso']:
                    # Intercambiar los datos de los nodos
                    actual.dato, actual.siguiente.dato = actual.siguiente.dato, actual.dato
                    cambiado = True
                actual = actual.siguiente



          ejercico 5
