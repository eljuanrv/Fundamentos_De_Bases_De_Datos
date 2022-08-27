
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
            idEmpleado=input('Ingresa el Numero de empleado: ')
            nombre=input('Ingresa tu nombre: ')
            apellidoP=input('Ingresa tu apellido paterno: ')
            apellidoM=input('Ingresa tu apellido materno: ')

            #-------------------------------------------------------------
            areas=open('Areas.txt','r')
            lista_de_areas=areas.readlines()
            lista_de_areas=lista_de_areas[1:]
            areas.close()

            cont=1
            claves_area=[]
            print('**********AREAS**********')
            for area in lista_de_areas:
                nombre_area=area.split()
                claves_area.append(nombre_area[0])
                nombre_area=nombre_area[1:]


                if len(nombre_area)>1:
                    nombre_area2=''
                    for palabra in nombre_area:
                        nombre_area2=nombre_area2+palabra+' '
                    nombre_area=nombre_area2.strip()
                else:
                    nombre_area=nombre_area[0]
                print(f'{cont}) {nombre_area}')
                cont+=1

            area=int(input('Ingresa el inciso de tu area: '))
            print()
            area=claves_area[area-1]
            puestos=open('Puestos.txt','r')
            lista_de_puestos=puestos.readlines()
            lista_de_puestos=lista_de_puestos[1:]
            areas.close()

            claves_puesto=[]
            lista_nombres_puestos=[]
            cont=1
            cont2=0
            lugar=[]
            print('**********PUESTOS**********')
            for puesto in lista_de_puestos:
                nombre_puesto=puesto.split()
                claves_puesto.append(nombre_puesto[0])
                clave_areaP=nombre_puesto[-1]
                nombre_puesto=nombre_puesto[1:-2]
                #print(nombre_puesto)
                
                #print(f'La clave es: {clave_areaP}, la area es: {area}')
                if clave_areaP==area:
                    if len(nombre_puesto)>1:
                        nombre_puesto2=''
                        for palabra in nombre_puesto:
                            nombre_puesto2=nombre_puesto2+palabra+' '
                        nombre_puesto=nombre_puesto2.strip()
                        print(f'{cont}) {nombre_puesto}')
                        lugar.append(cont2)
                        cont+=1
                        lista_nombres_puestos.append(nombre_puesto)
                        
                    else:
                        nombre_puesto=nombre_puesto[0]
                        
                        print(f'{cont}) {nombre_puesto}')
                        lugar.append(cont2)
                        cont+=1
                        lista_nombres_puestos.append(nombre_puesto)
                cont2+=1

            numero_puesto=int(input('Ingresa el inciso correspondiente al puesto: ')) 
            puesto=lista_nombres_puestos[numero_puesto-1]
            clave_nuevo_puesto='*'+claves_puesto[lugar[numero_puesto-1]]
            print()
            print('**********CLAVE**********')
            print(f'La clave de su puesto es: {clave_nuevo_puesto}')
            puesto=clave_nuevo_puesto

            #-------------------------------------------------------------
            
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

