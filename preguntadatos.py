#Aqui se preguntan datos con inputs
#Aqui se importa datetime para la fecha
import datetime

#Str - es una cadena de texto
#int - Numero natural
#Float - es un numero con decimales
#dt - es para fecha


def main():
 #con elinput ya esta predeterminado como cadena
 strDato = input("Dame un dato string: ")
 # se define una variable , la pregunta y luego se define como tipo entero.
 _iDato = input("Dame un dato entero: ")
 iDato = int(_iDato)
 _fDato = input("Dame un dato float: ")
 fDato =float(_fDato)
 # aqui se pregunta la fecha.
 _dtDato = input("Dame una fecha yyyy/mm/dd: ")
 # en los corchetes [a,b] se extrae desde la "a" hasta la "b" pero sin incluir "b" 

 # en [-a:] se extrae desde la primera posicion "a", de atras hacia delante, hasta que acabe

 anio=_dtDato[0:4]
 mes=_dtDato[5:7]
 dia=_dtDato[-2:]
 print(anio)
 print(mes)
 print(dia)

 dtDato = datetime.datetime(int(anio), int(mes), int(dia))

 print(strDato)
 print(type(strDato))
 print(iDato)
 print(type(iDato))
 print(fDato)
 print(type(fDato))
 print(dtDato)
 print(type(dtDato))