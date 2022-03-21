import threading

elementosNoAgregados = 5
elementosAProducir = threading.Semaphore(elementosNoAgregados)
elementosAConsumir = threading.Semaphore(0)
listaElementosEnUso = threading.Semaphore(1)
listaElementos = list()

def productor():
  while(True):
    elemento = "producto"
    elementosAProducir.acquire() #resta 1 a elementos que faltan por producir
    listaElementosEnUso.acquire() #evita que otros procesos usen la lista
    print("ingresando elemento a la lista en la posicion", len(listaElementos))
    print("elementos a producir: ", elementosAProducir._value, "elementos a consumir: ", elementosAConsumir._value+1)
    print("\n")
    listaElementos.append(elemento) #ingresa el elemento a la lista
    listaElementosEnUso.release() #libera la lista
    elementosAConsumir.release() #indica al consumidor que ya hay productos disponibles

def consumidor():
  while(True):
    elementosAConsumir.acquire() #resta 1 a elementos disponibles
    listaElementosEnUso.acquire() #evita que otros procesos usen la lista
    print("Consumiendo elemento de la lista en la posicion", len(listaElementos)-1)
    print("elementos a producir: ", elementosAProducir._value, "elementos a consumir: ", elementosAConsumir._value)
    print("\n")
    listaElementos.pop() #consumo elemento de la lista
    listaElementosEnUso.release() #libera la lista
    elementosAProducir.release() #indica al productor que puede ingresar elementos nuevos

def main():
  hiloProductor = threading.Thread(target=productor)
  hiloConsumidor = threading.Thread(target=consumidor)

  hiloProductor.start()
  hiloConsumidor.start()

main()
