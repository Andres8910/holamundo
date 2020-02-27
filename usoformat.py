def main():
  intBase = 7
  intAltura = 5
  fltAreaTriangulo = (intBase*intAltura)/2
  txt = "Area: {2:0.2f} ( {0} por {1} entre dos )"
  #el format sirve para darle una mejor presentacion
  print(txt.format(intBase, intAltura, fltAreaTriangulo))

#como se encuentran formados intbase, intaltura y fltareatriangulo seria desde 0, el intbase es 0 y intaltura es 1, pero aqui se usa nadamas 0 y 1

#{2:0.2f}
#en el 2 despues del punto son cuantos decimales se quieren utilizar 
#si se pone en vez de dos el 1 seria 17.5