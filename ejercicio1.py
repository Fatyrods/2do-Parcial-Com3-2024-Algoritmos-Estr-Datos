ejercicio 1

class fecha:
  def _init_(self, dia:none, mes:none, año:none):
    if dia is none or mes is none or año is none:
      hoy = datatime.today()
      self.dia=hoy.day
      self.mes=hoy.month
      self.año=hoy.year
    else:
      self.dia=dia
      self.mes=mes
      self.año=año
  def _str_(self):
    return f"{self.dia:06d}/{self.mes:01}/[self.año}"
  def _add_(self,dias):
   nueva_fecha=datatime (self.año, self.mes, self.dia) + timedelta(days=dias)
    return fecha(nueva fecha.day, nueva_fecha.month,nueva_fecha.year)
  def_eq_(self, otra_fecha):
    return (self.dia==otra_fecha.dia and
           self.mes==otra_fecha.mes and
           self:año==otra_fecha.año)
 def calcular_dif_fecha(self,otra_fecha):
     fecha1=datetime(self.año, self.mes, self.dia)
     fecha2=datetime(otra_fecha.año,otra_fecha.mes,otra_fecha.dia)
     diferencia= abs((fecha1-fecha2).days)
     return diferencia


ejercicio 2:

  


      
