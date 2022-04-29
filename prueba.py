#!Python
from datetime import date

class Portfolio:
  # stocks es un diccionario con llave: Ticker de la Accion y valor: la cantidad de acciones
  def __init__(self,stocks)
    self.Stock=stocks
  
  def profit(self,Date1,Date2):
  # entregar el profit entre 2 fechas.   
    
    inic=0
    dolla=0
    
    # Dolares ganados (o perdidos)
    for ticker,cantidad in self.Stock:
      (diff)=(ticker.Price(Date2)-ticker.Price(Date1))*cantidad
      dolla+=diff
      
    # Dolareces iniciales
    for ticker,cantidad in self.Stock:
      inicial=ticker.Price(Date1)*cantidad
      inic+=inicial
      
    # return dolla/inic
    # Anualizado
    porc_an=(date(Date2)-date(Date1)).days/365
      
    return (dolla/inic)*inic
  
