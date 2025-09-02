#Satuan tujuan = Celcius
#Fahrenheit-Celcius
def C_from_F (F): 
  return ((F-32)*5)/9

#Kelvin-Celcius
def C_from_K (K):
  return (K-273.15)


#Satuan tujuan = Fahrenheit
#Celcius-Fahrenheit
def F_from_C (C):
  return ((C*9)/5)+32

#Kelvin-Fahrenheit
def F_from_K (K):
  return ((K-273)*1.8)+32


#Satuan tujuan = Kelvin
#Celcius-Kelvin
def K_from_C (C):
  return (C+273.15)

#Fahrenheit-Kelvin
def K_from_F (F):
  return ((((F-32)*5)/9)+273.15)



