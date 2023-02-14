# Fundamentos_De_Bases_De_Datos 2da Oportunidad
Aquí llevo el seguimiento de mi materia de Fundamentos de Bases de Datos en mi segundo intento :)

## Clase 13/02/23

Continuamos trabajando con el manejo de archivos en Python

```py
#se crea la clase que contendrá todos los metodos
class llenarBD():
    def __init__(self):
        pass
    
    #Metodo para llenar la informacion de ciudades
    def llenarCiudades(self):
        #Ciudades(cve_ciudad, nombre, estado)
        archivo=open('Ciudades.txt','a')
        cve_ciudad=input('Ingresa la clave de tu ciudad ')
        nombre=input('Ingresa el nombre de la ciudad ')
        estado=input('Ingresa el estado correspondiente de la ciudad ')
        registro=cve_ciudad+' '+nombre+' '+estado+'\n'
        archivo.write(registro)
        archivo.close()

    #Metodo para llenar la informacion de clientes
    def llenarClientes(self):
        print()
        #Clientes(correo, direccion, telefono)cve_clientes
        correo=input('Ingresa el correo ')
        direccion=input('Ingresa la direccion ')
        telefono=input('Ingresa el telefono ')

        archivo=open('Ciudades.txt','r')
        registros=archivo.readlines()
        archivo.close()
        cont=1
        print()
        print('Elige la ciudad correspondiente: ')
        for i in registros:
            print(f'{cont}) {i}')
            cont+=1
        ciudad=int(input())
        registro_seleccionado=registros[ciudad-1]
        clave=registro_seleccionado[0:registro_seleccionado.find(' ')]

        archivo=open('Clientes.txt','a')
        registro=correo+' '+direccion+' '+telefono+' '+clave+'\n'
        archivo.write(registro)
        archivo.close()

    #Metodo para llenar la informacion de unidades
    def llenarUnidades(self):
        ###Unidades(matricula, tipo_unidad) CVE_EMP
        print()
        matricula=input('Ingresa la matricula ')
        tipo=input('Ingresa el tipo de unidad ')

        archivo=open('Empleados.txt','r')
        registros=archivo.readlines()
        archivo.close()
        cont=1
        print('Elige al empleado correspondiente: ')
        for i in registros:
            print(f'{cont}) {i}')
            cont+=1
        empleado=int(input())
        registro_seleccionado=registros[empleado-1]
        clave=registro_seleccionado[0:registro_seleccionado.find(' ')]

        archivo=open('Unidades.txt','a')
        registro=matricula+' '+tipo+' '+clave+'\n'
        archivo.write(registro)
        archivo.close()

    #Metodo para llenar la informacion de Empleados
    def llenarEmpleados(self):
        ##Empleados(cve_empleado, nombre, direccion, telefono, salario)
        archivo=open('Empleados.txt','a')
        cve_emp=input('Ingresa la clave del empleado ')
        nombre=input('Ingresa el nombre ')
        direccion=input('Ingresa la direccion ')
        telefono=input('Ingresa el telefono ')
        salario=input('Ingresa el salario ')
        registro=cve_emp+' '+nombre+' '+direccion+' '+telefono+' '+salario+'\n'
        archivo.write(registro)
        archivo.close()

#Hacemos la instanciación de la clase para poder utilizar los metodos de la misma
BD=llenarBD()

#se crea el menu con las diferentes opciones que tenemos.
#en cada opcion se hace la instancia del objeto correspondiente
#no estoy seguro de que asi se le llama :)
while True:
    opcion=int(input('''
    Selecciona una opcion
    1) llenar ciudades
    2) llenar empleados
    3) llenar unidades
    4) llenar clientes
    5) llenar paquetes
    6)salir
    '''))
    if opcion==1:
        BD.llenarCiudades()
    elif opcion==2:
        BD.llenarEmpleados()
    elif opcion==3:
        BD.llenarUnidades()
    elif opcion==4:
        BD.llenarClientes()
    else:
        break

```
