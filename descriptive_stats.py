import math
def promedio(vals):
  
  '''
  Calcula el promedio de una lista de números.
  Revisa y elimina posibles NaN en los datos.

  Parámetros:
  -------------
  vals: lista
        Lista con los números

  Retorna:
  -------------
  promedio: float
            Promedio de los números
  '''
  
  vals = [x for x in vals if not math.isnan(x)]
  if not vals:
    return float('NaN')
  
  promedio = sum(vals) / len(vals)
  return promedio



def mediana(vals):
  
  '''
  Calcula la mediana de una lista de datos.

  Parámetros:
  -------------
  vals: lista
        Lista con los datos.

  Retorna:
  -------------
  mediana: float
            La mediana de los datos.
  '''
  
  list_orden = sorted(vals)
  n = len(list_orden)
  
  if n % 2 == 0:
    m_1 = list_orden[n // 2 - 1]
    m_2 = list_orden[n // 2]
    return (m_1 + m_2) / 2
  else:
    return list_orden[n // 2]
  
  
  
def moda(vals):
    '''
    Calcula la moda de una lista de datos.

    Parámetros:
    -------------
    vals: lista
          Lista con los datos.

    Retorna:
    -------------
    moda: int
          La moda de los datos.
    '''
    
    categorias = []
    for i in vals:
      if i not in categorias:
        categorias.append(i)

    frec = []
    for categoria in categorias:
      contador = 0
      for i in vals:
        if i == categoria:
          contador += 1
      frec.append(contador)

    max_frec = 0
    for valor in frec:
      if valor > max_frec:
        max_frec = valor

    moda = []
    for i in range(len(categorias)):
      if frec[i] == max_frec:
        moda.append(categorias[i])

    if len(moda) == len(categorias) and len(categorias) > 1:
      return None
    if len(moda) == 1:
      return moda[0]

    return moda



def rango(vals):
  '''
  Calcula el rango de una lista de datos.

  Parámetros:
  -------------
  vals: lista
        Lista con los datos.

  Retorna:
  -------------
  rango: int
          El rango de los datos.
  '''

  return max(vals) - min(vals)



def varianza(vals, tipo = 'Poblacional'):
  '''
  Calcula la varianza poblacional de una lista de datos.
  A no ser que se espqcifieue que es muestrla.

  Parámetros:
  -------------
  vals: lista
        Lista con los datos.

  tipo: str
        Indica si la varianza se calcula como poblacional o muestral.
        Por defecto es poblacional.

  Retorna:
  -------------
  varianza: int
            La varianza de los datos.
  '''

  n = len(vals)
  if n <  2:
    return 0
  media = promedio(vals)

  dif_sqr = sum([(x- media)**2 for x in vals])

  if tipo == 'Muestral':
    denominador = n-1
  else:
    denominador = n

  varianza = dif_sqr/denominador
  return varianza



def desviacion_estandar(vals):
  '''
  Calcula la desviación estándar de los números.

  Parámetros:
  -------------
  vals: lista
        Lista con los números

  Retorna:
  --------------
  desviación estandar: float
        La desviación estandar de los números
  '''

  return math.sqrt(varianza(vals))



def desviacion_mediana_absoluta(vals):
  '''
  Calcula la desviación mediana absoluta de una lista de números.

  Parámetros:
  -------------
  vals: lista
        Lista con los números.

  Retorna:
  -------------
  desviación media absoluta: float
        La desviación media absoluta de la mediana de los números.
  '''

  med = mediana(vals)
  desv = [abs(x-med) for x in vals]
  return mediana(desv)



def percentil(vals, percentil):
  '''
  Calcula el percentil de una lista de números.

  Parámetros:
  -------------
  vals: lista
        Lista con los números.

  percentil: int
        Percentil a calcular.

  Retorna:
  -------------
  percentil: float 
        Percentil solicitado de una lista de números.
  '''

  list_orden = sorted(vals)
  n = len(list_orden)
  
  posicion = (percentil*(n-1)/100)
  pos_int = int(posicion)
  pos_dec = posicion - pos_int

  if pos_dec == 0:
    percentil = list_orden[pos_int]
  else:
    p_valor = list_orden[pos_int]
    s_valor = list_orden[pos_int + 1]
    percentil = p_valor + pos_dec * (s_valor - p_valor)

  return percentil



def rango_intercuartilico(vals):
  '''
  calcula el rango intercuartílico de una lista de números.

  Parámetros:
  -------------
  vals: lista
        Lista con los números.

  Retorna:
  -------------
  rango intercuartílico: float
        Rango intercuartílico de una lista de números.
  '''

  q_1 = percentil(vals, 25)
  q_3 = percentil(vals, 75)
  return q_3 - q_1



def covarianza(vals_x, vals_y):
  '''
  Calcula la covarianza de dos listas de números.
  Revisa y elimina valores NaN.

  Parámetros:
  -------------
  vals_x, vals_y: lista
        Lista con los dos atributos, las dos listas de números.

  Retorna:
  -------------
  covarianza: float
        Covarianza de los dos atributos.
  '''
  n = len(vals_x)
  if len(vals_y) != n:
    return 'Deben ser del mismo largo'
  if n < 2:
    return 0

  media_1 = promedio(vals_x)
  media_2 = promedio(vals_y)

  sum = 0
  for i in range(n):
    dif_x = vals_x[i] - media_1
    dif_y = vals_y[i] - media_2
    sum += dif_x * dif_y

  return sum/n



def correlación(vals_x, vals_y):
  '''
  Calcula la correlacion de dos listas de números.
  Revisa y elimina valores NaN.

  Parámetros:
  -------------
  vals_x, vals_y: lista
        Lista con los dos atributos, las dos listas de números.

  Retorna:
  -------------
  correlación: float
        Correlación de los dos atributos.
  '''
  desv_est_x = desviacion_estandar(vals_x)
  desv_est_y = desviacion_estandar(vals_y)
  if desv_est_x == 0 or desv_est_y == 0:
    return None
  else:
    return covarianza(vals_x, vals_y) / (desv_est_x * desv_est_y)
