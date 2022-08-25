# Fundamentos_De_Bases_De_Datos
Aquí llevo el seguimiento de mi materia de Fundamentos de Bases de Datos

## Clase 19/08/22

Unicamente vimos un repaso a la programacion con Python y recordamos la Programacion Orientada a Objetos con Python

1) Repaso

```py

from curses.ascii import isdigit
from re import A


entrada=input('Ingresa tu nombre: ')
#print(entrada)

for i in range(3):
    print(end=entrada)

longitud=len(entrada)
print(longitud)

caracter='a'
posicion=(entrada.find(caracter))
print(posicion)

lista=[]
while len(lista)<3:
    numero=input('Ingresa un numero: ')
    if numero.isdigit:
        numero=int(numero)
        lista.append(numero)
    else:
        print('No es un numero tonto :( ')
suma=lista[0]+lista[1]+lista[2]
resta=lista[0]-lista[1]-lista[2]
multiplicacion=lista[0]*lista[1]*lista[2]
print('Suma: '+str(suma))
print('Resta: '+str(resta))
print('Multiplicacion: '+str(multiplicacion))
```

2) POO

```py
class archivo:
    def __init__(self):
        print('')

    def crearArchivo(self):
        #open
        nombreA=input('Ingresa el nombre del archovo: ')
        nombreA=nombreA+'.txt'
        archivo=open(nombreA,'w')
        archivo.close()

    def escribirRegistro(self):
        #pedir nombre de archivo
        nombreA=input('Ingresa el nombre del archovo: ')
        nombreA=nombreA+'.txt'
        #cantidad de registros necesarios
        cantidad=int(input('Ingresa la cantidad de registros: '))

        registro=''
        #agregar archivo usa a
        archivo=open(nombreA,'a')
        for i in range(cantidad):
            numControl=int(input('Ingresa tu numero de control: '))
            nombre=input('Ingresa tu nombre: ')
            registro=registro+str(numControl)+' '+nombre+'\n'

        archivo.write(registro)
        archivo.close()

    def leerRegistro(self):
        #pedir nombre de archivo
        nombreA=input('Ingresa el nombre del archovo: ')
        nombreA=nombreA+'.txt'
        archivo=open(nombreA,'r')

        registros=archivo.read()
        archivo.close()
        print(registros)

        archivo=open(nombreA,'r')
        registros2=archivo.readlines()
        archivo.close()
        print(registros2)

        cont=1
        for registro in registros2:
            print(f'{cont}) {registro}')
            cont+=1


app=archivo()
#app.crearArchivo()
#app.escribirRegistro()
app.leerRegistro()
```

## Clase 22/08/22

Realizamos la primera actividad para entregar

```py
#Juan Rivera Vargas Fundamentos de Bases de Datos

class archivo:
    def __init__(self):
        print('')
    #crear archivo
    def crearArchivo(self):
        #open
        nombreA=input('Ingresa el nombre del archivo: ')
        nombreA=nombreA+'.txt'
        archivo=open(nombreA,'w')
        archivo.close()
    
    #leer archivo
    def leerArchivo(self):
        #pedir nombre de archivo
        nombreA=input('Ingresa el nombre del archivo: ')
        nombreA=nombreA+'.txt'
        archivo=open(nombreA,'r')
        registros2=archivo.readlines()
        archivo.close()

        cont=1
        for registro in registros2:
            print(f'{cont}) {registro}')
            cont+=1

    #ingresar registros
    def ingresarRegistro(self):
        #pedir nombre de archivo
        nombreA=input('Ingresa el nombre del archivo: ')
        nombreA=nombreA+'.txt'
        #cantidad de registros necesarios
        cantidad=int(input('Ingresa la cantidad de registros: '))

        registro=''
        #agregar archivo usa a
        archivo=open(nombreA,'a')
        for i in range(cantidad):
            idEmpleado=input('Ingresa el ID: ')
            nombre=input('Ingresa tu nombre: ')
            apellidoP=input('Ingresa tu apellido paterno: ')
            apellidoM=input('Ingresa tu apellido materno: ')
            puesto=input('Ingresa tu puesto: ')
            puesto='*'+puesto
            sueldo=int(input('Ingresa tu sueldo: '))
            sueldo='$'+str(sueldo)
            registro=registro+idEmpleado+' '+nombre+' '+apellidoP+' '+apellidoM+' '+puesto+' '+sueldo+'\n'

        archivo.write(registro)
        archivo.close()

    
    #editar registros
    def editarRegistro(self):
        #pedir nombre de archivo
        nombreA=input('Ingresa el nombre del archivo: ')
        nombreA=nombreA+'.txt'
        archivo=open(nombreA,'r')
        registros2=archivo.readlines()
        archivo.close()

        cont=1
        for registro in registros2:
            print(f'{cont}) {registro}')
            cont+=1

        editar=int(input('Ingresa el inciso correspondiente al empleado que quieres editar: '))
        print()
        print('Que campo deseas editar?')
        print('Campo 2: Nombre')
        print('Campo 3: Apellido paterno')
        print('Campo 4: Apellido materno')
        print('Campo 5: Puesto')
        print('Campo 6: Sueldo')

        opcion=int(input('Ingresa la opcion correspondiente al campo que deseas editar: '))

        if opcion ==2:
            print('Editando Nombre')
        elif opcion==3:
            print('Editando Apellido Paterno')
        elif opcion==4:
            print('Editando Apellido Materno')
        elif opcion==5:
            print('Editando Puesto')
        elif opcion==6:
            print('Editando Sueldo')
        else: print('Esa opcion no esta en la lista')

opcion=1
while opcion != 5:
    print('Ingresa el numero correspondiente a la opcion que quieras realizar')
    print('1) Crear archivo')
    print('2) Leer archivo')
    print('3) Ingresar registros')
    print('4) Editar registros')
    print('5) Salir')
    opcion=int(input())

    app=archivo()
    if opcion ==1:
        app.crearArchivo()
    elif opcion==2:
        app.leerArchivo()
    elif opcion==3:
        app.ingresarRegistro()
    elif opcion==4:
        app.editarRegistro()
    elif opcion==5:
        print('Adios, vuelva pronto')
    else: print('Esa opcion no esta en la lista')
```

## Clase 24/08/22

- Continuamos con el manejo de archivos

```py
#Juan Rivera Vargas Fundamentos de Bases de Datos

class archivo:
    def __init__(self):
        print('')
    #crear archivo
    def crearArchivo(self):
        #open
        nombreA=input('Ingresa el nombre del archivo: ')
        nombreA=nombreA+'.txt'
        archivo=open(nombreA,'w')
        archivo.close()
    
    #leer archivo
    def leerArchivo(self):
        #pedir nombre de archivo
        nombreA=input('Ingresa el nombre del archivo: ')
        nombreA=nombreA+'.txt'
        archivo=open(nombreA,'r')
        registros2=archivo.readlines()
        archivo.close()

        cont=1
        for registro in registros2:
            print(f'{cont}) {registro}')
            cont+=1

    #ingresar registros
    def ingresarRegistro(self):
        #pedir nombre de archivo
        nombreA=input('Ingresa el nombre del archivo: ')
        nombreA=nombreA+'.txt'
        #cantidad de registros necesarios
        cantidad=int(input('Ingresa la cantidad de registros: '))

        registro=''
        #agregar archivo usa a
        archivo=open(nombreA,'a')
        for i in range(cantidad):
            idEmpleado=input('Ingresa el ID: ')
            nombre=input('Ingresa tu nombre: ')
            apellidoP=input('Ingresa tu apellido paterno: ')
            apellidoM=input('Ingresa tu apellido materno: ')
            puesto=input('Ingresa tu puesto: ')
            puesto='*'+puesto
            sueldo=int(input('Ingresa tu sueldo: '))
            sueldo='$'+str(sueldo)
            registro=registro+idEmpleado+' '+nombre+' '+apellidoP+' '+apellidoM+' '+puesto+' '+sueldo+'\n'

        archivo.write(registro)
        archivo.close()

    
    #editar registros
    def editarRegistro(self):
        #pedir nombre de archivo
        nombreA=input('Ingresa el nombre del archivo: ')+'.txt'
        #abrimos el archivo en modo lectura
        archivo=open(nombreA,'r')
        registros2=archivo.readlines()
        archivo.close()

        #creamos un archivo auxiliar para ir almacenando la informacion
        archivoAux=open('archivoAux.txt','a')

        #mostramos la lista de registros para que elija 1
        cont=1
        for registro in registros2:
            print(f'{cont}) {registro}')
            cont+=1
        editar=int(input('Ingresa el inciso correspondiente al empleado que quieres editar: '))
        editar=editar-1
        registroE=registros2[editar]

        #mostramos la informacion del registro que eligio anteriormente
        print(f'La informacion actual es: {registroE}')
        print()
        print('Que campo deseas editar?')
        print('Campo 2: Nombre')
        print('Campo 3: Apellido paterno')
        print('Campo 4: Apellido materno')
        print('Campo 5: Puesto')
        print('Campo 6: Sueldo')
        opcion=int(input('Ingresa la opcion correspondiente al campo que deseas editar: ')) 
        
        #cada palabra del registro la separamos en una nueva cadena
        listaCampos=registroE.split()
        #esta variable nos indica si hubo alguna modificacion de los registros
        modificar=0
        #Es la opcion para editar el nombre
        if opcion ==2:
            #el segundo campo de la lista corresponde al nombre
            print(f'El nombre actual es: {listaCampos[1]}')
            nombreN=input('Ingresa el nuevo nombre: ')
            #reemplazamos el valor anterior del nombre
            listaCampos[1]=nombreN
            modificar=1
        #Opcion para editar el apellido paterno
        elif opcion==3:
            #el tercer campo de la lista corresponde al apellido paterno
            print(f'El apellido paterno es: {listaCampos[2]}')
            apellidoP=input('Ingresa el nuevo apellido paterno: ')
            #reemplazamos el valor anterior del apellido paterno
            listaCampos[2]=apellidoP
            modificar=1
        #Opcion para editar el apellido materno
        elif opcion==4:
            #el cuarto campo de la lisat correspode al apellido materno
            print(f'El apellido materno es: {listaCampos[3]}')
            apellidoM=input('Ingresa el nuevo apellido materno: ')
            #reemplazamos el valor anterior del apellido materno
            listaCampos[3]=apellidoM
            modificar=1
        #Opcion para editar el puesto
        elif opcion==5:
            #el quinto campo corresponde al puesto
            print(f'El puesto es: {listaCampos[4][1:]}')
            puestoN=input('Ingresa el nuevo puesto: ')
            #reemplazamos el valor anterior del puesto
            listaCampos[4]='*'+puestoN
            modificar=1
        #Opcion para editar el sueldo
        elif opcion==6:
            #el sexto campo corrsponde al sueldo
            print(f'El sueldo es: {listaCampos[5][1:]}')
            sueldoN=input('Ingresa el nuevo sueldo: ')
            #reemplazamos el valor anterior del sueldo
            listaCampos[5]='$'+sueldoN
            modificar=1

        else: 
            print('Esa opcion no esta en la lista')
            archivoAux.close()

        #en este registro se concatenan cada uno de los campos ingresados aneriormente
        registros4=''
        for i in range(len(listaCampos)):
            if i<len(listaCampos)-1:
                registros4=registros4+listaCampos[i]+' '
            else:
                registros4=registros4+listaCampos[i]+'\n'
        #si se modifico algun campo se sustituye el nuevo registro en la lista original de registros
        if modificar != 0:
            registros2[editar]=registros4
        for registro in registros2:
            archivoAux.write(registro)
        archivoAux.close()

#Ciclo para elegir cualquiera de las opciones a realizar
opcion=1
while opcion != 5:
    print('Ingresa el numero correspondiente a la opcion que quieras realizar')
    print('1) Crear archivo')
    print('2) Leer archivo')
    print('3) Ingresar registros')
    print('4) Editar registros')
    print('5) Salir')
    opcion=int(input())

    app=archivo()
    if opcion ==1:
        app.crearArchivo()
    elif opcion==2:
        app.leerArchivo()
    elif opcion==3:
        app.ingresarRegistro()
    elif opcion==4:
        app.editarRegistro()
    elif opcion==5:
        print('Adios, vuelva pronto')
    else: print('Esa opcion no esta en la lista')
```
