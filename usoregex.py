#EN ESTE PROGRAMA SE PREGUNTA UN DATO HASTA QUE SEA CORRECTO Y LUEGO SE VALIDA

# AQUI SE IMPORTA EL MODULO RE PARA USAR EXRESIONES
import re

def main():
  # Infinty loop - repite hasta que este un break y se acaba, si no se escribe bien se va estar repitiendo
  while True:
    strRFC = input("Dame el RFC: ")
    coincide = re.search("^[A-Z]{4}-[0-9]{6}-[A-Z0-9]{3}$", strRFC)
    if (coincide):
      print("RFC Correcto!")
      break
    else:
      print("RFC incorrecto. Intenta de nuevo.")