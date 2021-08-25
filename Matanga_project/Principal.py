import psycopg2
import xlrd

from Creacion_db import *
import pandas as pd


# CON ESTE ARCHIVO CREAS CURSOS NUEVOS, CREAS TABLAS DE EJERCICIOS Y LAS LLENAS
#TAMBIEN PASAS TABLAS A EXCEL

#ABAJO DE TODO ESTÁN LOS CÓDIGOS Q LOS LANZAN



cursos = {} #En este diccionario se crearán los cursos/tabla con armar_tabla_curso()
            #Se podrá eventualmente agregar más elementos con la función agregar_estudiante()

class Principal():

    def armar_tabla_curso():

        print()
        print("########################################################################################")
        print("###############################   BIENVENIDO :)   ######################################")
        print("########################################################################################")
        print()

        #Conectando
        conn = psycopg2.connect(
            host = 'localhost',
            database = 'instanciaMarzo',
            port = 5432,
            user = 'postgres',
            password = 'postgres'
        )

 
        conn.autocommit = True  

        #Cursor
        cursor = conn.cursor()


       
        listaTemporal = []
        #cursos = {}
        print("Termine todo el proceso hasta el final para que los datos se guarden correctamente.")
        print("__________________________________________________________________________________")
        print()
        
        while True:
            print("-- A CADA CURSO CREADO LE CORRESPONDE UNA NUEVA TABLA --\nLos nombres de tablas no admiten espacios, ni empezar con nros o mayúscula.\
                \nEmpiece siempre con un caracter en minúscula.\n")

            while True:
                #CURSO ------------------------
                
                curso = input("Formato definitivo a usar ejemplo: 'real_3ro_1ra'\n\
                    \nNUEVO CURSO A CREAR: ")

                try:
                    cursor.execute(f"SELECT * FROM {curso}")
                    print("________________________________________________________")
                    print()
                    print("---> Esa tabla ya existe. Intente con otra. <---")
                    print()

                except:
                    print("-------")
                    break


            while True:
                while True: 
                    #NOMBRE ------------------------
                    print()
                    nombre = input(f"Nombre del/a estudiante de {curso}: ")

                    nombreValidacion = ''.join(nombre.split()) #Quitando los espacios intermedios
                    nombreValidacion = ''.join(nombreValidacion.split(',')) #Quitando las comas

                    if nombreValidacion.isalpha() == False:
                        print()
                        print("---> Ingresó un nombre incorrecto. No ingrese números. <---")
                        print()
                    
                    else:
                        print("-------")
                        print()
                        break

                
                while True: 
                    #DNI ------------------------
                    
                    dni = input("Ingresá DNI(sin puntos) - No ingreses nada si deseás completar después.\nDNI: ")

                    dniValidacion = ''.join(dni.split('.'))

                    if dniValidacion.isdigit() == True:
                        print()
                        print("----------------------------------------------------")
                        break

                    elif dni == '':
                        dni = None
                        print()
                        print("----------------------------------------------------")
                        break

                    else:
                        print()
                        print("--> Ingresá solo números, sin puntos ni espacio <--")
                        print()



                #Agregando a la lista temporal
                listaTemporal.append([nombre, dni])



                while True:
                    opcion_estudiante= input(f"YA HAY {len(listaTemporal)} ESTUDIANTES EN EL CURSO: {curso}.\
                        \n----------------------------------------------------\
                        \n[1] - Agregar otro/a estudiante.\n[2] - Dejar de ingresar estudiantes para el curso {curso}.\
                        \nSU ELECCIÓN: " )
                    if opcion_estudiante != '1' and opcion_estudiante != '2':
                        print()
                        print("--->  Ingrese 1 o 2. No otro número  <---")
                        print()
                    else:
                        break

                if opcion_estudiante == '2':
                    # Creando el diccionario y agregando los datos de los estudiantes cargados
                    cursos.setdefault(curso, listaTemporal)
                    listaTemporal=[]
                    print()
                    print(f"Saliendo de la tabla del CURSO: {curso} ...")
                    print()
                    print("--------------------------------------------")
                    print()
                    break

                else:
                    print()
                    print(f"Procediendo a agregar otro estudiante de {curso}...")
                    print()
            


            while True:
                eleeccion_curso = input("[1] - AGREGAR OTRO CURSO.\n[2] - Dejar de ingresar cursos.\
                    \nSU ELECCIÓN: ") 
                if eleeccion_curso != '1' and eleeccion_curso != '2':
                    print("Ingrese 1 o 2. No otro número")
                else:
                    break

            if eleeccion_curso == '1':
                print()
                print("Procediendo a agregar otro curso.")
                print()


            if eleeccion_curso == '2':
                print()
                print("Saliendo del programa de creacion de tablas por curso.")
                print(f"Se crearon {len(list(cursos))} cursos(tablas)")
                print()
                
                break

        
        
        #FINALIZANDO EL WHILE - SUBIR A BASE DE DATOS:
       
        


        #Creando la tabla SEGÚN NUESTRO DICCIONARIO
        for cant_tablas in range(len(list(cursos))):  #Debe ir entre comillas dobles porque tiene números. Ej: 3ro 1ra
            cursor.execute (f"""CREATE TABLE "{list(cursos)[cant_tablas]}" (
                ID SERIAL PRIMARY KEY NOT NULL,
                Estudiante VARCHAR(100),
                DNI VARCHAR (50))""")




        #------------------------------------------------------------------------------------------------------------------------------
        #Luego de crear la tabla ya se puede
        def generar_headers(nombre_diccionario):                  # USANDO SCHEMA POR DEFAULT                             #La tabla ya recibe el nombre de cada key
            cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_schema = 'public' AND table_name = '{list(nombre_diccionario)[0]}'")
                                                                                    # DENTRO DE SCHEMA USANDO PUBLIC POR DEFECTO 


            #Esto no crea tablas, solo necesitamos como parámetro a una sola, la primera al menos SOLO para sacar 
            # sus headers (lo que nos interesa)
            #FUNCIONA CON LISTA DE LISTAS DENTRO DEL KEY Y CON UNO O MÁS KEYS


            temporal = cursor.fetchall()
            headers = [] #Haremos una lista pulida de encabezados
            for i in range(len(temporal)-1): #No se tomará el valor [0] SI USAS ID PK AUTOCOPMLETADO POR ESO EL -1 (AJUSTAR)
                headers.append(temporal[i+1][0])
            headers= ', '.join(headers) #Unimos todo separando por comas y espacio para hacer desaparecer comillas internas 
            
            return headers
            #HEADERS LISTOS PARA USAR (CON ID AUTOCOMPLETADO - AJUSTAR QUITANDOLE EL -1 Y +1 SI NO HAY ID PK)





        def generar_valores(cada_estudiante):

            values = []
            #Aquí tenés dos opciones o el DNI existe o es None.

            for i in range(len(cada_estudiante)): #Ver cuántos valores tiene cada tabla
                if cada_estudiante[i] == None:
                    values.append('Null') #En join se le quitan las comillas e ira null al final para SQL
                    
                
                else:
                    valor = "'" + cada_estudiante [i] + "'"   # ES NECESARIO SOBRECOMILLAR LOS STR 
                    values.append(valor) #En este caso ambos son str sí o sí para esta tabla (Ajustar en tablas distintas)

            values = ", ".join(values) #CON ESTE JOIN DESAPARECERAN LAS COMILLAS DEL INT Y LA COMILLA EXTRA DEL STR

            return values #Listo para usarse en sentencia SQL


        def crear_Tabla_enDB(nombre_diccionario):
            #Se creará y ejecutará una sintaxis SQL para subir a DB por cáda key creada en un diccionario según requerimiento de tabla
            
            for cadaTabla in range(len(list(nombre_diccionario))):
                for cada_estudiante in nombre_diccionario.get(list(nombre_diccionario)[cadaTabla]):
                    print(f"En la tabla: {list(nombre_diccionario)[cadaTabla]} se agregó {generar_valores(cada_estudiante)}")
                    cursor.execute(f"INSERT INTO {list(nombre_diccionario)[cadaTabla]} ({generar_headers(nombre_diccionario)}) VALUES ({generar_valores(cada_estudiante)})")
                print("-------")

        #------------------------------------------------------------------------------------------------------------------------------


        #EJECUTANDO FUNCIONES PARA CREAR LA BASE DE DATOS
        print("Generando headers")
        print(generar_headers(cursos))
        print()
        print("generando valores")
        print(generar_valores(cursos.get( list(cursos) [0] ) [0] ))
        print()

        crear_Tabla_enDB(cursos)
        print()
        print("Proceso terminado con éxito.")
        print("Hasta luego :)")
        print()
        



# Hacer un código para modificar nombre de tabla

#Hacer código bajar y subir a excel para resguardo

#Hacer código para modificar o agregar un valor de la tabla

#Hacer codigo para modificar tabla agregar o quitar estudiantes

'''
    def modificar_tabla(): 
        print("-------------------------------------------------------------------------------------")
        print("-------------------------  Hola. Modifiquemos una tabla  ----------------------------")
        print("-------------------------------------------------------------------------------------")
        print()
        print()
'''






#______________________________________________________________________________________________________________________

class Main_Ejercicios(): 

    




    def crear_tabla_ejercicios(nombre_tabla, tabla_foranea, id_tabla_foranea): #AJUSTAR SIEMPRE AL TIPO DE DATOS DE EJERCICIOS QUE NECESITES - LO MISMO EN CREACION_DB
        #Conectando
        conn = psycopg2.connect(
            host = 'localhost',
            database = 'instanciaMarzo',
            port = 5432,
            user = 'postgres',
            password = 'postgres'
        )


        conn.autocommit = True  

        #Cursor
        cursor = conn.cursor()
        

        #Cada dato sera único:
        #Tabla con id primary - ej_9_a (INT) - ej_9_b (INT) - ej_9_c1 (INT) - ej_9_c2 (INT) - ej_9_c3 (INT) -   
                             #- ej_11 (INT) - ej_13_a (VARCHAR binario8) - ej_13_b (VARCHAR binario8) - ej_14 (INT)  
                                                      # un binario de 8 cifras en str

        
        #Creando tabla automáticamente según cantidad de estudiantes de la tabla del curso, utilizando su clave primaria
        #Puse que todos sean varchar porque hay números con ceros adelante.. si necesito operarlos luego los paso a int
        cursor.execute(f"""CREATE TABLE {nombre_tabla}(
            ID SERIAL PRIMARY KEY NOT NULL,
            EJ_9_A VARCHAR(10),
            EJ_9_B VARCHAR(10),
            EJ_9_C1 VARCHAR(10),
            EJ_9_C2 VARCHAR(10),
            EJ_9_C3 VARCHAR(10),
            EJ_11 VARCHAR(10),
            EJ_13_A VARCHAR(10),
            EJ_13_B VARCHAR(10),
            EJ_14 VARCHAR(10),
            ID_ALUMNO INTEGER REFERENCES {tabla_foranea} ({id_tabla_foranea}))
        """) #CREAR LA FOREIGN KEY EN UNA SOLA LINEA ES MUCHO MÁS FÁCIL
        
        print(f"Creación de la tabla {nombre_tabla} terminado. Esta tabla referencia a la PK({id_tabla_foranea}) de la tabla {tabla_foranea}")




    def llenar_tabla_ejercicios(nombre_tabla, tabla_foranea):
        #Conectando
        conn = psycopg2.connect(
            host = 'localhost',
            database = 'instanciaMarzo',
            port = 5432,
            user = 'postgres',
            password = 'postgres'
        )


        conn.autocommit = True  

        #Cursor
        cursor = conn.cursor()




        #Conocer cuantos encfabezados hay
        cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_schema = 'public' AND table_name = '{nombre_tabla}'")
        temporal = cursor.fetchall()
        
        headers = [] #Haremos una lista pulida de encabezados
        for i in range(len(temporal)-1): #No se tomará el valor [0] SI USAS ID PK AUTOCOPMLETADO POR ESO EL -1 (AJUSTAR)
            headers.append(temporal[i+1][0])
        headers= ', '.join(headers) #Unimos todo separando por comas y espacio para hacer desaparecer comillas internas 
        
        #HEADERS LISTOS PARA USAR (CON ID AUTOCOMPLETADO - AJUSTAR QUITANDOLE EL -1 Y +1 SI NO HAY ID PK)

        estudiantes = 0


        #Conocer cantidad de registros(estudiantes) que hay en la tabla elegida
        cursor.execute(f"SELECT COUNT(*) FROM {tabla_foranea}")
        estudiantes = cursor.fetchall()[0][0] #Los [0][0] es para eliminar su tupla dentro de una lista así da solo el int


        values = []
        
        
        #Creando el objeto para operar la clase ejercicios del archivo Creacion_db
        ejercicios = Alerta_ejercicios()
            
        for cada_estudiante in range(estudiantes): #Se hara una tupla grande según sus atributos(columnas)
            
            #Agregando uno a uno los ejercicios
            values.append(ejercicios.aleatorio_amper())
            values.append(ejercicios.aleatorio_cable())
            tupla_temporal = ejercicios.aleatorio_amperes()
            lista_temporal = list(tupla_temporal)
            values = values + lista_temporal
            values.append(ejercicios.aleatorio_watts())
            tupla_temporal2 = ejercicios.aleatorio_binario()
            lista_temporal = list(tupla_temporal2)
            values = values + lista_temporal
            values.append(ejercicios.aleatorio_gigas())
            values.append(cada_estudiante +1) #El id de lista estudiantes empieza por el 1

                        
            
            #Formatearemos la lista para la sintaxis SQL - 
            
            valores_SQL = []
            #CUANDO SE LLENA VALORES EN SQL SIEMPRE LOS STR LLEVAN COMILLA, LOS INT NO!
            for cada_dato in range(len(values)):
                
                if values[cada_dato] == None:
                    valores_SQL.append('Null') #En join se le quitan las comillas e ira null al final para SQL
                
                        #COMO TENES BINARIOS MEJOR QUE TODO SEA STR - LUEGO LO PASAS A INT CUANDO HAGA FALTA OPERAR

                else:
                    valor = "'" + str(values[cada_dato]) + "'"   # ES NECESARIO SOBRECOMILLAR LOS STR 
                    valores_SQL.append(valor) #En este caso ambos son str sí o sí para esta tabla (Ajustar en tablas distintas)

            valores_SQL = ", ".join(valores_SQL) #CON ESTE JOIN DESAPARECERAN LAS COMILLAS DEL INT Y LA COMILLA EXTRA DEL STR

            #Listo para usarse en sentencia SQL


            #CARGANDO LA TABLA CON CADA REGISTRO A LA VEZ

            cursor.execute(f"INSERT INTO {nombre_tabla} ({headers}) VALUES({valores_SQL})")

            #Proceso finalizado
            values = [] #Hay que reiniciar el valor inicial de valores para que no se sume valores sobre otros
            print(f"Llenado de la tabla {nombre_tabla} terminado.")
            
    #EJERCICIOS DE 4TO AÑO  ERAN SOLO PREGUNTAS
    #CUIDADO DE QUE EN LA TABLA DE DB ESTE TODO EN MINUSCULAS PARA LLENARLA SINO DIRA QUE NO HAR RELACION Y NO EXISTE LA COLUMNA
    def llenar_tabla_ejercicios_4to(nombre_tabla, tabla_foranea):
        #Conectando
        conn = psycopg2.connect(
            host = 'localhost',
            database = 'instanciaMarzo',
            port = 5432,
            user = 'postgres',
            password = 'postgres'
        )


        conn.autocommit = True  

        #Cursor
        cursor = conn.cursor()




        #Conocer cuantos encfabezados hay
        cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_schema = 'public' AND table_name = '{nombre_tabla}'")
        temporal = cursor.fetchall()
        
        headers = [] #Haremos una lista pulida de encabezados
        for i in range(len(temporal)-1): #No se tomará el valor [0] SI USAS ID PK AUTOCOPMLETADO POR ESO EL -1 (AJUSTAR)
            headers.append(temporal[i+1][0])
        headers= ", ".join(headers) #Unimos todo separando por comas y espacio para hacer desaparecer comillas internas 
        
        print(headers)

        #HEADERS LISTOS PARA USAR (CON ID AUTOCOMPLETADO - AJUSTAR QUITANDOLE EL -1 Y +1 SI NO HAY ID PK)
    
        estudiantes = 0

        
        #Conocer cantidad de registros(estudiantes) que hay en la tabla elegida
        cursor.execute(f"SELECT COUNT(*) FROM {tabla_foranea}")
        estudiantes = cursor.fetchall()[0][0] #Los [0][0] es para eliminar su tupla dentro de una lista así da solo el int
        
        
        cursor.execute(f"SELECT * FROM {tabla_foranea}")
        datos_estudiante = cursor.fetchall()
        
        
        values = []
        
        
        #Creando el objeto para operar la clase ejercicios del archivo Creacion_db
        #ejercicios = Alerta_ejercicios()
            
        for cada_estudiante in range(estudiantes): #Se hara una tupla grande según sus atributos(columnas)
            
            #Agregando uno a uno los ejercicios

            values.append(False)
            values.append(None)
            values.append(None)
            
            values.append(False)
            values.append(None)
            values.append(None)

            values.append(False)
            values.append(None)
            values.append(None)

            values.append(False)
            values.append(None)
            values.append(None)

            values.append(False)
            values.append(None)
            values.append(None)

            values.append(False)
            values.append(None)
            values.append(None)

            values.append(False)
            values.append(None)
            values.append(None)

            values.append(False)
            values.append(None)
            values.append(None)

            values.append(False)
            values.append(None)
            values.append(None)

            values.append(False)
            values.append(None)
            values.append(None)

            values.append(False)
            values.append(None)
            values.append(None)

            values.append(False)
            values.append(None)
            values.append(None)

            values.append(False)
            values.append(None)
            values.append(None)

            values.append(False)
            values.append(None)
            values.append(None)

            values.append(False)
            values.append(None)
            values.append(None)

            values.append(False)
            values.append(None)
            values.append(None)

            values.append(False)
            values.append(None)
            values.append(None)

            values.append(False)
            values.append(None)
            values.append(None)

            values.append(False)
            values.append(None)
            values.append(None)

            values.append(False)
            values.append(None)
            values.append(None)

            values.append(False)
            values.append(None)
            values.append(None)

            values.append(False) #Da igual porque en esta columna en este orden siempre es false
            values.append(datos_estudiante[cada_estudiante][0])

                        
            
            #Formatearemos la lista para la sintaxis SQL - 
            
            valores_SQL = []
            #CUANDO SE LLENA VALORES EN SQL SIEMPRE LOS STR LLEVAN COMILLA, LOS INT NO!
            for cada_dato in range(len(values)):
                
                if values[cada_dato] == None:
                    valores_SQL.append("Null") #En join se le quitan las comillas e ira null al final para SQL
                
                        #COMO TENES BINARIOS MEJOR QUE TODO SEA STR - LUEGO LO PASAS A INT CUANDO HAGA FALTA OPERAR

                else:
                    valor = "'" + str(values[cada_dato]) + "'"   # ES NECESARIO SOBRECOMILLAR LOS STR 
                    valores_SQL.append(valor) #En este caso ambos son str sí o sí para esta tabla (Ajustar en tablas distintas)

            valores_SQL = ", ".join(valores_SQL) #CON ESTE JOIN DESAPARECERAN LAS COMILLAS DEL INT Y LA COMILLA EXTRA DEL STR

           

            #Listo para usarse en sentencia SQL

            
            #CARGANDO LA TABLA CON CADA REGISTRO A LA VEZ

            cursor.execute(f"INSERT INTO {nombre_tabla} ({headers}) VALUES({valores_SQL})")

            #Proceso finalizado
            values = [] #Hay que reiniciar el valor inicial de valores para que no se sume valores sobre otros
            print(f"Llenado de la tabla {nombre_tabla} terminado.")
            


            
    #EJERCICIOS DE 3ER AÑO  
    #CUIDADO DE QUE EN LA TABLA DE DB ESTE TODO EN MINUSCULAS PARA LLENARLA SINO DIRA QUE NO HAR RELACION Y NO EXISTE LA COLUMNA
    def llenar_tabla_ejercicios_3ro(nombre_tabla, tabla_foranea):
        #Conectando
        conn = psycopg2.connect(
            host = 'localhost',
            database = 'instanciaMarzo',
            port = 5432,
            user = 'postgres',
            password = 'postgres'
        )


        conn.autocommit = True  

        #Cursor
        cursor = conn.cursor()


        #Conocer cuantos encfabezados hay
        cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_schema = 'public' AND table_name = '{nombre_tabla}'")
        temporal = cursor.fetchall()
        
        headers = [] #Haremos una lista pulida de encabezados
        for i in range(len(temporal)-1): #No se tomará el valor [0] SI USAS ID PK AUTOCOPMLETADO POR ESO EL -1 (AJUSTAR)
            headers.append(temporal[i+1][0])
        headers= ", ".join(headers) #Unimos todo separando por comas y espacio para hacer desaparecer comillas internas 
        
 

        #HEADERS LISTOS PARA USAR (CON ID AUTOCOMPLETADO - AJUSTAR QUITANDOLE EL -1 Y +1 SI NO HAY ID PK)
    
        estudiantes = 0

        
        #Conocer cantidad de registros(estudiantes) que hay en la tabla elegida
        cursor.execute(f"SELECT COUNT(*) FROM {tabla_foranea}")
        estudiantes = cursor.fetchall()[0][0] #Los [0][0] es para eliminar su tupla dentro de una lista así da solo el int
        
        
        cursor.execute(f"SELECT * FROM {tabla_foranea}")
        datos_estudiante = cursor.fetchall()
        
        for d in datos_estudiante:
            print (d[0])
        
        values = []
        
        #print("valores", values) 
        #Creando el objeto para operar la clase ejercicios del archivo Creacion_db
        #ejercicios = Alerta_ejercicios()
        print(".......................")
        for cada_estudiante in range(estudiantes): #Se hara una tupla grande según sus atributos(columnas)
            
            #Agregando uno a uno los ejercicios
            
            values.append(False)
            values.append(None)
            values.append(None)

            values.append(False)
            values.append(None)
            values.append(None)

            values.append(False)
            values.append(None)
            values.append(None)

            values.append(False)
            values.append(None)
            values.append(None)

            values.append(False)
            values.append(None)
            values.append(None)

            values.append(False)
            values.append(None)
            values.append(None)

            values.append(False)
            values.append(None)
            values.append(None)

            values.append(False)
            values.append(None)
            values.append(None)

            values.append(False)
            values.append(None)
            values.append(None)
            
            values.append(False)
            values.append(None)
            values.append(None)

            values.append(False)
            values.append(None)
            values.append(None)

            values.append(False)
            values.append(None)
            values.append(None)

            values.append(False)
            values.append(None)
            values.append(None)

            values.append(False)
            values.append(None)
            values.append(None)

            values.append(False)
            values.append(None)
            values.append(None)

            values.append(False)
            values.append(None)
            values.append(None)


            values.append(datos_estudiante[cada_estudiante][0])
            

                                   
            
            #Formatearemos la lista para la sintaxis SQL - 
            
            valores_SQL = []
            #CUANDO SE LLENA VALORES EN SQL SIEMPRE LOS STR LLEVAN COMILLA, LOS INT NO!
            for cada_dato in range(len(values)):
                
                if values[cada_dato] == None:
                    valores_SQL.append("Null") #En join se le quitan las comillas e ira null al final para SQL
                
                        #COMO TENES BINARIOS MEJOR QUE TODO SEA STR - LUEGO LO PASAS A INT CUANDO HAGA FALTA OPERAR

                else:
                    valor = "'" + str(values[cada_dato]) + "'"   # ES NECESARIO SOBRECOMILLAR LOS STR 
                    valores_SQL.append(valor) #En este caso ambos son str sí o sí para esta tabla (Ajustar en tablas distintas)

            valores_SQL = ", ".join(valores_SQL) #CON ESTE JOIN DESAPARECERAN LAS COMILLAS DEL INT Y LA COMILLA EXTRA DEL STR

           

            #Listo para usarse en sentencia SQL

            
            #CARGANDO LA TABLA CON CADA REGISTRO A LA VEZ

            cursor.execute(f"INSERT INTO {nombre_tabla} ({headers}) VALUES({valores_SQL})")

            #Proceso finalizado
            values = [] #Hay que reiniciar el valor inicial de valores para que no se sume valores sobre otros
            print(f"Llenado de la tabla {nombre_tabla} terminado.")
            




class Resguardo ():

    def pasar_a_excel(nombre_tabla, nombre_archivo_xlsx):
        #Conectando
        conn = psycopg2.connect(
            host = 'localhost',
            database = 'instanciaMarzo',
            port = 5432,
            user = 'postgres',
            password = 'postgres'
        )


        conn.autocommit = True  

        #Cursor
        cursor = conn.cursor()
        print("================================")

        #conocer encabezados
        cursor.execute(f"SELECT column_name FROM information_schema.columns \
            WHERE table_schema = 'public' AND table_name = '{nombre_tabla}'")
        encabezados_puros = cursor.fetchall()
        
        encabezados = []
        for i in encabezados_puros: #Debo quitarles sus corchetes y parentesis
            encabezados.append(i[0])


        #Conocer cantidad de encabezados
        cant_encabezados = len(encabezados)

        #Conocer cantidad de registros
        cursor.execute(f"SELECT COUNT(*) FROM {nombre_tabla}")
        cant_filas = cursor.fetchall()

        # Crear el diccionario para subir a excel, cada key es encabezado columna 
        # y sus values los valores, los valores de toda la columna

        dic_para_excel = {} #Creando el diccionario de columnas que usaremos para subir al excel

        #Codigo para reutilizar
        #Llenando el diccionario con cualquiera fuera las columnas que tenga.
        for atributo in range(cant_encabezados):
            dic_para_excel.setdefault(encabezados[atributo], [])

        #Llenado de ese diccionario con append... cada key es encabezado de CADA COLUMNA
        for fila in range(cant_filas[0][0]): #[0][0] para quitarle su corchete y parentesis
            for columna in range(len(encabezados)):
                cursor.execute(f"SELECT * FROM {nombre_tabla} WHERE id='{fila+1}'")
                estudiante = cursor.fetchall()
                estudiante =  estudiante[0] #Debo quitarle el [] o saldra del rango luego

                #Agregando uno a uno en cada iteración
                dic_para_excel.get(list(dic_para_excel)[columna]).append(estudiante[columna])
                
        #Del la BD se pasa al data frame y del data frame al excel.. siempre el data frame de intermedio
        data_frame = pd.DataFrame(dic_para_excel, columns= (list(dic_para_excel)))
                    #pd es panda.. lo importe al panda como as pd


        
        # Eliminá el archivo excel si vas a quitar este comentario
        #print(r'nombre_archivo_xlsx')

        # Probemos ahora sin quitarle los índices
        
'''
=============================================================================
'''

class Main_Datos(): 
    #cON AGREGAR DATOS SE AGREGAN LOS DATOS A COLUMNAS YA CREADAS. bORRA LA SEÑAL #------ CLAVE 2 PARA USAR SOLO UNA CLAVE FORANEA
                                                                #ELIMINÁ ESTO si necesitas utilizar un solo pk
                                                                #Y elimina tmb abajo el pedido y los agregados
    def agregar_datos_soluciones_3ro(nombre_tabla, tabla_foranea, tabla_foranea2):
        

        #Conectando
        conn = psycopg2.connect(
            host = 'localhost',
            database = 'instanciaMarzo',
            port = 5432,
            user = 'postgres',
            password = 'postgres'
        )


        conn.autocommit = True  

        #Cursor
        cursor = conn.cursor()


        #Conocer cuantos encfabezados hay
        cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_schema = 'public' AND table_name = '{nombre_tabla}'")
        temporal = cursor.fetchall()
        
        headers = [] #Haremos una lista pulida de encabezados
        for i in range(len(temporal)-1): #No se tomará el valor [0] SI USAS ID PK AUTOCOPMLETADO POR ESO EL -1 (AJUSTAR)
            headers.append(temporal[i+1][0])
        headers= ", ".join(headers) #Unimos todo separando por comas y espacio para hacer desaparecer comillas internas 


        #HEADERS LISTOS PARA USAR (CON ID AUTOCOMPLETADO - AJUSTAR QUITANDOLE EL -1 Y +1 SI NO HAY ID PK)
    

        estudiantes = 0

   
        # DATOS DE TABLA EJERCICIOS - QUE DAN CUENTA DE LA CANTIDAD DE ESTUDIANTES
        #Conocer cantidad de registros(estudiantes-la misma cantidad en tabla ejercicios-) que hay en la tabla foranea elegida
        cursor.execute(f"SELECT COUNT(*) FROM {tabla_foranea}")
        estudiantes = cursor.fetchall()[0][0] #Los [0][0] es para eliminar su tupla dentro de una lista así da solo el int
        
        
        cursor.execute(f"SELECT * FROM {tabla_foranea}")
        datos_estudiante = cursor.fetchall()
        
        
        values = []

        #print("valores", values) 
        #Creando el objeto para operar la clase ejercicios del archivo Creacion_db
        #ejercicios = Alerta_ejercicios()
        for d in datos_estudiante:
            print(d[0])

        print("_-------------")
        
        # Esto será por cada estudiante- fila ejercicio   
        for cada_estudiante in range(estudiantes): #Se hara una tupla grande según sus atributos(columnas)
            
            cursor.execute(f"SELECT * FROM {tabla_foranea2}") #--------------------------------- BORRAR CLAVE FORANEA2
            dato_ejercicio = cursor.fetchall() #------------------------------------------------ BORRAR CLAVE FORANEA2

            print(dato_ejercicio[cada_estudiante][0]) #----------------------------------------- BORRAR CLAVE FORANEA2

            
            #Como es una iteración que va sumándose es necesario reiniciar los datos
            #Me di cuenta luego que esto no hacía falta pero igual lo dejé
            sol_punto_9_a = 0
            sol_punto_9_b = 0
            sol_9_suma_amperes = 0
            sol_punto_9_c = 0
            sol_11_resultado_watt = 0
            sol_punto_11 = 0
            sol_punto_13_a_128 = 0
            sol_punto_13_a_64 = 0
            sol_punto_13_a_32 = 0
            sol_punto_13_a_16 = 0
            sol_punto_13_a_8 = 0
            sol_punto_13_a_4 = 0
            sol_punto_13_a_2 = 0
            sol_punto_13_a_1 = 0
            sol_punto_13_a = 0
            sol_punto_13_b_128 = 0
            sol_punto_13_b_64 = 0
            sol_punto_13_b_32 = 0
            sol_punto_13_b_16 = 0
            sol_punto_13_b_8 = 0
            sol_punto_13_b_4 = 0
            sol_punto_13_b_2 = 0
            sol_punto_13_b_1 = 0
            sol_punto_13_b = 0
            sol_punto_14_mb = 0
            sol_punto_14_kb = 0
            sol_punto_14_b = 0
            sol_punto_14_kib = 0
            sol_punto_14_mib = 0
            sol_punto_14_gib = 0


            #Agregando uno a uno los ejercicios
            #______________________________________________________________ Creación datos ejercicios

            #Eliminar tabla de referencia. No hará falta para llegar a la solución

            
            if int(datos_estudiante[cada_estudiante][1]) >= 1 and int(datos_estudiante[cada_estudiante][1]) <= 9.6:
                sol_punto_9_a = '1'
            elif int(datos_estudiante[cada_estudiante][1]) >= 9.7 and int(datos_estudiante[cada_estudiante][1]) <= 13:
                sol_punto_9_a = '1.5'
            elif int(datos_estudiante[cada_estudiante][1]) >= 13.1 and int(datos_estudiante[cada_estudiante][1]) <= 18:
                sol_punto_9_a = '2.5'
            elif int(datos_estudiante[cada_estudiante][1]) >= 18.1 and int(datos_estudiante[cada_estudiante][1]) <= 24:
                sol_punto_9_a = '4'
            elif int(datos_estudiante[cada_estudiante][1]) >= 24.1 and int(datos_estudiante[cada_estudiante][1]) <= 31:
                sol_punto_9_a = '6'
            elif int(datos_estudiante[cada_estudiante][1]) >= 31.1 and int(datos_estudiante[cada_estudiante][1]) <= 43:
                sol_punto_9_a = '10'
            elif int(datos_estudiante[cada_estudiante][1]) >= 43.1 and int(datos_estudiante[cada_estudiante][1]) <= 63:
                sol_punto_9_a = '16'


            #Aquí tampoco se evidencia la necesidad de tabla

            if float(datos_estudiante[cada_estudiante][2]) == 1:
                sol_punto_9_b = '9.6'
            elif float(datos_estudiante[cada_estudiante][2]) == 1.5:
                sol_punto_9_b = '13'
            elif float(datos_estudiante[cada_estudiante][2]) == 2.5:
                sol_punto_9_b = '18'
            elif float(datos_estudiante[cada_estudiante][2]) == 4:
                sol_punto_9_b = '24'
            elif float(datos_estudiante[cada_estudiante][2]) == 6:
                sol_punto_9_b = '31'
            elif float(datos_estudiante[cada_estudiante][2]) == 10:
                sol_punto_9_b = '43'
            elif float(datos_estudiante[cada_estudiante][2]) == 16:
                sol_punto_9_b = '63'

            
            #Punto 9) c)

            #Hace falta una columna para el resultado de la suma
            sol_9_suma_amperes = int(datos_estudiante[cada_estudiante][3]) + int(datos_estudiante[cada_estudiante][4]) + int(datos_estudiante[cada_estudiante][5])

            #Y otra columna para el resultado final 
            if sol_9_suma_amperes >= 1 and sol_9_suma_amperes <= 9.6:
                sol_punto_9_c = '1'
            elif sol_9_suma_amperes >= 9.7 and sol_9_suma_amperes <= 13:
                sol_punto_9_c = '1.5'
            elif sol_9_suma_amperes >= 13.1 and sol_9_suma_amperes <= 18:
                sol_punto_9_c = '2.5'
            elif sol_9_suma_amperes >= 18.1 and sol_9_suma_amperes <= 24:
                sol_punto_9_c = '4'
            elif sol_9_suma_amperes >= 24.1 and sol_9_suma_amperes <= 31:
                sol_punto_9_c = '6'
            elif sol_9_suma_amperes >= 31.1 and sol_9_suma_amperes <= 43:
                sol_punto_9_c = '10'
            elif sol_9_suma_amperes >= 43.1 and sol_9_suma_amperes <= 63:
                sol_punto_9_c = '16'


            #Punto 11

            # Hara falta una columa para los amperes
            sol_11_resultado_watt = str(round(float(datos_estudiante[cada_estudiante][6]) / 220 , 2 ))

            

            #Otra columna para el resultado
            if float(sol_11_resultado_watt) >= 1 and float(sol_11_resultado_watt) <= 9.6:
                sol_punto_11 = '1'
            elif float(sol_11_resultado_watt) >= 9.7 and float(sol_11_resultado_watt) <= 13:
                sol_punto_11 = '1.5'
            elif float(sol_11_resultado_watt) >= 13.1 and float(sol_11_resultado_watt) <= 18:
                sol_punto_11 = '2.5'
            elif float(sol_11_resultado_watt) >= 18.1 and float(sol_11_resultado_watt) <= 24:
                sol_punto_11 = '4'
            elif float(sol_11_resultado_watt) >= 24.1 and float(sol_11_resultado_watt) <= 31:
                sol_punto_11 = '6'
            elif float(sol_11_resultado_watt) >= 31.1 and float(sol_11_resultado_watt) <= 43:
                sol_punto_11 = '10'
            elif float(sol_11_resultado_watt) >= 43.1 and float(sol_11_resultado_watt) <= 63:
                sol_punto_11 = '16'


            # Punto 13

            #Hará falta una columna para cada uno de estos datos
            sol_punto_13_a_128 = str(int(datos_estudiante[cada_estudiante][7][0]) * 128)
            sol_punto_13_a_64 = str(int(datos_estudiante[cada_estudiante][7][1]) * 64)
            sol_punto_13_a_32 = str(int(datos_estudiante[cada_estudiante][7][2]) * 32)
            sol_punto_13_a_16 = str(int(datos_estudiante[cada_estudiante][7][3]) * 16)
            sol_punto_13_a_8 = str(int(datos_estudiante[cada_estudiante][7][4]) * 8)
            sol_punto_13_a_4 = str(int(datos_estudiante[cada_estudiante][7][5]) * 4)
            sol_punto_13_a_2 = str(int(datos_estudiante[cada_estudiante][7][6]) * 2)
            sol_punto_13_a_1 = str(int(datos_estudiante[cada_estudiante][7][7]) * 1)

            #Y uno para la solucion
            sol_punto_13_a = int(sol_punto_13_a_128) + int(sol_punto_13_a_64)  + int(sol_punto_13_a_32)  + int(sol_punto_13_a_16)  + int(sol_punto_13_a_8)  + int(sol_punto_13_a_4)  + int(sol_punto_13_a_2)  + int(sol_punto_13_a_1) 


            #Luego hacer mas tablas para estos resultados otra vez para el punto b)
            #Hará falta una columna para cada uno de estos datos
            sol_punto_13_b_128 = str(int(datos_estudiante[cada_estudiante][8][0]) * 128)
            sol_punto_13_b_64 = str(int(datos_estudiante[cada_estudiante][8][1]) * 64)
            sol_punto_13_b_32 = str(int(datos_estudiante[cada_estudiante][8][2]) * 32)
            sol_punto_13_b_16 = str(int(datos_estudiante[cada_estudiante][8][3]) * 16)
            sol_punto_13_b_8 = str(int(datos_estudiante[cada_estudiante][8][4]) * 8)
            sol_punto_13_b_4 = str(int(datos_estudiante[cada_estudiante][8][5]) * 4)
            sol_punto_13_b_2 = str(int(datos_estudiante[cada_estudiante][8][6]) * 2)
            sol_punto_13_b_1 = str(int(datos_estudiante[cada_estudiante][8][7]) * 1)

            #Y uno para la solucion
            sol_punto_13_b = int(sol_punto_13_b_128) + int(sol_punto_13_b_64)  + int(sol_punto_13_b_32)  + int(sol_punto_13_b_16)  + int(sol_punto_13_b_8)  + int(sol_punto_13_b_4)  + int(sol_punto_13_b_2)  + int(sol_punto_13_b_1) 


            #Punto 14
            #Hará falta una columna para cada uno de estos datos
            sol_punto_14_mb = str(int(datos_estudiante[cada_estudiante][9]) * 1000)

            sol_punto_14_kb = str(int(sol_punto_14_mb) * 1000)

            sol_punto_14_b = str(int(sol_punto_14_kb) * 1000)

            sol_punto_14_kib = str(int(sol_punto_14_b) / 1024)

            sol_punto_14_mib = str(round(float(sol_punto_14_kib)/1024 , 2))

            sol_punto_14_gib = str(round(float(sol_punto_14_mib)/1024 , 2))


            #______________________________________________________________ Creación datos ejercicios


            #Agregando los datos en el mismo orden en el que está en la tabla
            values.append(sol_punto_9_a)
            values.append(sol_punto_9_b)

            values.append(sol_9_suma_amperes)
            values.append(sol_punto_9_c)
            values.append(sol_11_resultado_watt)

            values.append(sol_punto_11)
            values.append(sol_punto_13_a_128)

            values.append(sol_punto_13_a_64)
            values.append(sol_punto_13_a_32)

            values.append(sol_punto_13_a_16)
            values.append(sol_punto_13_a_8)

            values.append(sol_punto_13_a_4)
            values.append(sol_punto_13_a_2)

            values.append(sol_punto_13_a_1)
            values.append(sol_punto_13_a)

            values.append(sol_punto_13_b_128)
            values.append(sol_punto_13_b_64)

            values.append(sol_punto_13_b_32)
            values.append(sol_punto_13_b_16)

            values.append(sol_punto_13_b_8)
            values.append(sol_punto_13_b_4)

            values.append(sol_punto_13_b_2)
            values.append(sol_punto_13_b_1)
            
            values.append(sol_punto_13_b)
            
            values.append(sol_punto_14_mb)
            values.append(sol_punto_14_kb)

            values.append(sol_punto_14_b)
            values.append(sol_punto_14_kib)

            values.append(sol_punto_14_mib)
            values.append(sol_punto_14_gib)

            #ES IMPORTANTE QUE RESPETES EL ORDEN .. SI HAY ALGUN PROBLEMA FIJATE EN EL ORDEN DE LAS COLUMNAS Y AJUSTÁ
            #values.append(False) #Este es el mismo en todos asi que siempre sera false es la columna "aprobo_todo"
            
            
            
            values.append(dato_ejercicio[cada_estudiante][0]) #---------------------------------------- BORRAR CLAVE FORANEA2
            
            
            values.append(datos_estudiante[cada_estudiante][0]) #clave foranea 1

            print(values)
                                    

            #Formatearemos la lista para la sintaxis SQL - 
               
            valores_SQL = []
            #CUANDO SE LLENA VALORES EN SQL SIEMPRE LOS STR LLEVAN COMILLA, LOS INT NO!
            for cada_dato in range(len(values)):
                
                if values[cada_dato] == None:
                    valores_SQL.append("Null") #En join se le quitan las comillas e ira null al final para SQL
                
                        #COMO TENES BINARIOS MEJOR QUE TODO SEA STR - LUEGO LO PASAS A INT CUANDO HAGA FALTA OPERAR

                else:
                    valor = "'" + str(values[cada_dato]) + "'"   # ES NECESARIO SOBRECOMILLAR LOS STR 
                    valores_SQL.append(valor) #En este caso ambos son str sí o sí para esta tabla (Ajustar en tablas distintas)

            valores_SQL = ", ".join(valores_SQL) #CON ESTE JOIN DESAPARECERAN LAS COMILLAS DEL INT Y LA COMILLA EXTRA DEL STR

            #Listo para usarse en sentencia SQL

            
            #CARGANDO LA TABLA CON CADA REGISTRO A LA VEZ

            cursor.execute(f"INSERT INTO {nombre_tabla} ({headers}) VALUES({valores_SQL})")

            #Proceso finalizado
            values = [] #Hay que reiniciar el valor inicial de valores para que no se sume valores sobre otros
            
            
          
        print(f"Llenado de la tabla {nombre_tabla} terminado.")



        
        # Eliminá el archivo excel si vas a quitar este comentario
        #print(r'nombre_archivo_xlsx')

        # Probemos ahora sin quitarle los índices
        
        
        ######################################################
        ########  SEGURIDAD - SEGURIDAD - SEGURIDAD  #########
        ######################################################
        
        print("SEGURIDAD: VERI SI ESTÁ COMENTADO EL GUARDADO PARA QUE NO SOBREESCRIBAS ALGÚN EXCEL EXISTENTE")
        #data_frame.to_excel(f'Resguardo\{nombre_archivo_xlsx}', index=False, header=True)
        print("Ver si está comentado. Si no lo está, verás que no se creó el archivo")





    def agregar_un_dato_3ro(nombre_tabla, tabla_foranea):
        

        #Conectando
        conn = psycopg2.connect(
            host = 'localhost',
            database = 'instanciaMarzo',
            port = 5432,
            user = 'postgres',
            password = 'postgres'
        )


        conn.autocommit = True  

        #Cursor
        cursor = conn.cursor()


        #Conocer cuantos encfabezados hay
        cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_schema = 'public' AND table_name = '{nombre_tabla}'")
        temporal = cursor.fetchall()
        
        headers = [] #Haremos una lista pulida de encabezados
        for i in range(len(temporal)-1): #No se tomará el valor [0] SI USAS ID PK AUTOCOPMLETADO POR ESO EL -1 (AJUSTAR)
            headers.append(temporal[i+1][0])
        headers= ", ".join(headers) #Unimos todo separando por comas y espacio para hacer desaparecer comillas internas 


        #HEADERS LISTOS PARA USAR (CON ID AUTOCOMPLETADO - AJUSTAR QUITANDOLE EL -1 Y +1 SI NO HAY ID PK)
    

        estudiantes = 0

   
        # DATOS DE TABLA EJERCICIOS - QUE DAN CUENTA DE LA CANTIDAD DE ESTUDIANTES
        #Conocer cantidad de registros(estudiantes-la misma cantidad en tabla ejercicios-) que hay en la tabla foranea elegida
        cursor.execute(f"SELECT COUNT(*) FROM {tabla_foranea}")
        estudiantes = cursor.fetchall()[0][0] #Los [0][0] es para eliminar su tupla dentro de una lista así da solo el int
        
        
        cursor.execute(f"SELECT * FROM {tabla_foranea}")
        datos_estudiante = cursor.fetchall()
        
        
        values = []

        #print("valores", values) 
        #Creando el objeto para operar la clase ejercicios del archivo Creacion_db
        #ejercicios = Alerta_ejercicios()



        
        
        # Esto será por cada estudiante- fila ejercicio   
        for cada_estudiante in range(estudiantes): #Se hara una tupla grande según sus atributos(columnas)
            


            #Agregando los datos en el mismo orden en el que está en la tabla

            values.append(datos_estudiante[cada_estudiante][0])
            

            print(values)
                                    

            #Formatearemos la lista para la sintaxis SQL - 
               
            valores_SQL = []
            #CUANDO SE LLENA VALORES EN SQL SIEMPRE LOS STR LLEVAN COMILLA, LOS INT NO!
            for cada_dato in range(len(values)):
                
                if values[cada_dato] == None:
                    valores_SQL.append("Null") #En join se le quitan las comillas e ira null al final para SQL
                
                        #COMO TENES BINARIOS MEJOR QUE TODO SEA STR - LUEGO LO PASAS A INT CUANDO HAGA FALTA OPERAR

                else:
                    valor = "'" + str(values[cada_dato]) + "'"   # ES NECESARIO SOBRECOMILLAR LOS STR 
                    valores_SQL.append(valor) #En este caso ambos son str sí o sí para esta tabla (Ajustar en tablas distintas)

            valores_SQL = ", ".join(valores_SQL) #CON ESTE JOIN DESAPARECERAN LAS COMILLAS DEL INT Y LA COMILLA EXTRA DEL STR

            #Listo para usarse en sentencia SQL

            
            #CARGANDO LA TABLA CON CADA REGISTRO A LA VEZ

            cursor.execute(f"INSERT INTO {nombre_tabla} ({headers}) VALUES({valores_SQL})")

            #Proceso finalizado
            values = [] #Hay que reiniciar el valor inicial de valores para que no se sume valores sobre otros
        

          
        print(f"Llenado de la tabla {nombre_tabla} terminado.")



        
        # Eliminá el archivo excel si vas a quitar este comentario
        #print(r'nombre_archivo_xlsx')

        # Probemos ahora sin quitarle los índices
        
        
        ######################################################
        ########  SEGURIDAD - SEGURIDAD - SEGURIDAD  #########
        ######################################################
        
        print("SEGURIDAD: VERI SI ESTÁ COMENTADO EL GUARDADO PARA QUE NO SOBREESCRIBAS ALGÚN EXCEL EXISTENTE")
        #data_frame.to_excel(f'Resguardo\{nombre_archivo_xlsx}', index=False, header=True)
        print("Ver si está comentado. Si no lo está, verás que no se creó el archivo")




#ESTE CÓDIGO PASA UNA TABLA DE BASE DE DATOS A UN EXCEL#
#Resguardo.pasar_a_excel('ejer_previas_marzo2021_tecno', 'exel_tabla_ejercicios_previa.xlsx')


        
#HABILITÁ ESTE CÓDIGO PARA CREAR UN NUEVO CURSO/TABLA
#Principal.armar_tabla_curso()



        
#Crear luego un Principal para elegir siempre si crear mas tablas de curso o lo q fuera

#PRIMERO SE CREA LA TABLA EJERCICIO
#Crear la tabla - automatizalo xq no sabés cuantas instancias de exámenes habrá (tabla nueva, tabla foranea, referencia PK foranea)
#Main_Ejercicios.crear_tabla_ejercicios('ejer_previas_marzo2021_tecno', 'real_previas_marzo2021_tecnologia','id')


#LUEGO SE LA LLENA la tabla de ejercicio
#Llenar la tabla según cantidad de alumnos de la tabla foreign
#Main_Ejercicios.llenar_tabla_ejercicios_4to("estudiantes_correcciones_4to_2da", "real_4to_2da")

#LLENAR TABLA 3ro
#Main_Ejercicios.llenar_tabla_ejercicios_3ro("estudiantes_correcciones_3ro_2da", 'ejer_real_3ro_2da')

#LLENAR UNA TABLA la de soluciones de ejercicios
#Main_Datos.agregar_datos_soluciones_3ro('estudiantes_soluciones_previa_3ro', 'ejer_previas_marzo2021_tecno')


Main_Datos.agregar_datos_soluciones_3ro('estudiantes_soluciones_3ro_2da', 'ejer_real_3ro_2da', 'estudiantes_correcciones_3ro_2da')