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

### Descripción del metodo llenar unidades
- Metodo para llenar la informacion de unidades
```py
    
    def llenarUnidades(self):
        #Atrubutos de la entidad unidades
        ###Unidades(matricula, tipo_unidad) CVE_EMP
        
        #Primero nos ingresan la matricula y el tipo, los pedimos primero porque los ingresan directamente
        print()
        matricula=input('Ingresa la matricula ')
        tipo=input('Ingresa el tipo de unidad ')
```
- Necesitamos la clave de empleados por eso es necesario abrir el archivo de empleados en modo lectura y utilizamos el metodo **readlines** para guardar cada renglon del archivo empleados en un elemento de una lista como la siguiente

```py
['E001 SAUL RIOS 34 5342342 133\n', 'E002 JUAN RIOS 34 5342342 132\n', 'E003 Maria Rios 36 894383 233\n']
```
Y el for se utiliza para imprimir cada elemento de esa lista
```py
        archivo=open('Empleados.txt','r')
        registros=archivo.readlines()
        archivo.close()
        cont=1
        print('Elige al empleado correspondiente: ')
        for i in registros:
            print(f'{cont}) {i}')
            cont+=1
```
Despues de mostrar el menu le pedimos que ingrese el numero correspondiente al empleado
```py
        empleado=int(input())
```
La variable registros contiene la lista de todos los empleados y nosotros solo necesitamos el empleado que seleccionó en el menu
Ya que los indices de las listas inician en **0** y nuestro menu inicia en **1** debemos restarle 1 al momento de acceder al elemento de la lista correspondiente.
```py
        registro_seleccionado=registros[empleado-1]
```
Ya que tenemos seleccionado el registro debemos tomar unicamente la clave, para eso utilizamos el metodo [find](https://www.freecodecamp.org/espanol/news/tutorial-de-metodos-de-cadena-de-texto-en-python-como-usar-find-y-replace-en-python/#:~:text=El%20m%C3%A9todo%20find%20%28%29%20busca%20a%20trav%C3%A9s%20de,Si%20this_pattern%20no%20est%C3%A1%20en%20this_string%2C%20retorna%20-1.), debido a que la el elemento guardado en la variable *registro seleccionado* tiene el siguiente formato 
```py
'E001 SAUL RIOS 34 5342342 133\n'
```
Necesitamos utilizar find para que encuentre el primer espacio en blanco y apartir de ahí [cortar](https://phytoneando.top/python-cortar-cadenas/#:~:text=El%20troceado%20de%20cadenas%20en%20Python%20sigue%20siempre,rango%20de%20caracteres%20utilizando%20la%20sintaxis%20de%20corte.) la cadena, y eso se logra con la siguiente instruccion.
```py
        clave=registro_seleccionado[0:registro_seleccionado.find(' ')]
```
Y por ultimo se abre el archivo de unidades y se le agrega el nuevo registro
```py
        archivo=open('Unidades.txt','a')
        registro=matricula+' '+tipo+' '+clave+'\n'
        archivo.write(registro)
        archivo.close()
```
