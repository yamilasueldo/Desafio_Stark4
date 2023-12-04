import re
from data_stark import lista_personajes

def validar_lista(lista:list)->bool:
    '''
    Valida que una lista sea del tipo lista y no este vacia
    Parametros: lista(list) -> lista a validar
    Retorno: un booleano que representa si la lista es valida
    '''
    es_valida = False
    if(isinstance(lista,list) and len(lista) > 0):
        es_valida = True
    return es_valida

def validar_lista_diccionario(lista:list)->bool:
    '''
    Valida que todos los elementos de una lista sean del tipo dict
    Parametros: lista(list) -> lista a validar
    Retorno: un booleano, True si todos los elementos de la lista son del tipo dict, False si al menos un elemento no lo es
    '''
    es_lista_diccionario = True
    for elemento in lista:
        if(type(elemento) != dict):
            es_lista_diccionario = False
            break
    return es_lista_diccionario

#1.1
def extraer_iniciales(nombre_heroe:str)->str:
    '''
    Devuelve las iniciales en base a un nombre
    Parametros: nombre_heroe(str) -> nombre del que saco las iniciales
    Retorno: string de la iniciales del nombre, o 'N/A' si el nombre_heroe es vacio
    '''
    if(len(nombre_heroe) > 0):
        nombre_separado = re.split("-| the | ", nombre_heroe)
        iniciales = ''
        for nombre in nombre_separado:
            iniciales += nombre[0].upper() + '.'
    else:
        iniciales = "N/A"
    return iniciales 

#1.2
def obtener_dato_formato(dato:str)->str:
    '''
    Convierte un dato a formato de texto y reemplaza espacios y guiones por guiones bajos.
    Parámetros: dato(str) -> El dato que se desea formatear.
    Retorno: un string -> El dato formateado.
    '''
    retorno = False
    if(type(dato) == str):
        dato = dato.lower()
        retorno = re.sub(' |-', '_',dato)
    return retorno

#1.3
def obtener_nombre_con_iniciales(heroe:dict)->str: 
    '''
    Obtiene el nombre de un héroe y lo formatea con iniciales.
    Parámetros:  heroe (dict)-> El diccionario que contiene la información del héroe.
    Retorna: un string -> El nombre del héroe formateado con iniciales.
    '''
    retorno = False
    if(type(heroe) == dict and 'nombre' in heroe):
        retorno = '* ' + obtener_dato_formato(heroe['nombre']) + ' (' + extraer_iniciales(heroe['nombre']) +')'
    return retorno

#1.4
def stark_imprimir_nombres_con_iniciales(lista_personajes:list)->bool:
    '''
    Imprime los nombres de los personajes con iniciales formateados.
    Parámetros: lista_personajes(list) -> La lista de personajes a imprimir.
    Retorna:   booleano(bool) -> True si se imprimieron nombres exitosamente, False si la lista de personajes no es válida.
    '''
    retorno = False
    if(validar_lista(lista_personajes)):
        for personaje in lista_personajes:
            print(obtener_nombre_con_iniciales(personaje))
            retorno = True
    return retorno

#2.1
def generar_codigo_heroe(heroe:dict,id:int)->str:
    '''
    Genera un código de héroe basado en el género y un número de identificación.
    Parámetros: heroe(dict) -> El diccionario que contiene la información del héroe.
                id(int) -> El número de identificación del héroe.
    Retorna:
        un string -> El código de héroe generado.
    '''
    codigo = 'N/A'
    genero = (heroe['genero'])
    if genero in ['M','F','NB']:
        if genero == 'M':
            digito = '1'
        elif genero == 'F':
            digito = '2'
        else:
            digito = '0'
        id = str(id)
        cantidad_ceros = 9 - (len(genero) + len(id))
        codigo = genero + '-' + digito + (id).zfill(cantidad_ceros)
    return codigo 

def agregar_codigo_heroe(heroe:dict,codigo:str)->None:
    '''
    Agrega un código de héroe a un diccionario de héroe.
    Parámetros: heroe(dict) -> El diccionario que contiene la información del héroe.
                codigo(str) -> El código de héroe a agregar.
    '''
    heroe['codigo_heroe'] = codigo

#2.2 
def stark_generar_codigos_heroes(lista_heroes:list):
    '''
    Genera códigos de héroes para una lista de héroes y los agrega a los diccionarios de héroes.
    Imprime los nombres de los héroes y sus códigos.
    Parámetros: lista_heroes(list) -> La lista de héroes a procesar.
    Retorna: un string -> Una cadena que contiene los nombres de héroes y sus códigos.
    '''
    if (len(lista_heroes) > 0 and validar_lista_diccionario(lista_heroes)):
        codigos = ''
        contador_codigos = 0
        for i in range(len(lista_heroes)):
            nombre_personaje = obtener_nombre_con_iniciales(lista_heroes[i]) + ' | ' 
            codigo_personaje = generar_codigo_heroe(lista_heroes[i],i+1)
            agregar_codigo_heroe(lista_heroes[i],codigo_personaje)
            codigos += nombre_personaje + codigo_personaje + '\n'
            contador_codigos += 1
        print(codigos)
        print ("Se asignaron {} codigos".format(contador_codigos))
    else:
        codigos = False
    return codigos
#3.1
def sanitizar_entero(numero_str)->int:
    '''
    Analiza el string recibido y determina si es un número
    entero positivo.
    Parametros: numero_str:str -> un string que representa un posible número entero
    Retorno: un entero 
            -1 -> si numero_str contienen caracteres no númericos
            -2 -> si numero_str es un numero negativo
            -3 -> si ocurre algun error al intertar convertir numero_str en entero
            el string recibido casteado a entero -> si el string es un numero entero positivo 
    '''
    numero_str = numero_str.strip()
    if(not numero_str.isdigit()):
        retorno = -1
    else:
        if(int(numero_str) < 0):
            retorno = -2
        else:
            try:
                numero = int(numero_str) 
                retorno = numero 
            except ValueError: 
                retorno = -3
    return retorno

#3.2
def sanitizar_flotante(numero_str:str)->int:
    '''
    Analiza el string recibido y determina si es un número
    flotante positivo.
    Parametros: numero_str:str -> un string que representa un posible número decimal
    Retorno: un entero negativo
            -1 -> si numero_str contienen caracteres no númericos
            -2 -> si numero_str es un numero negativo
            -3 -> si ocurre algun error al intertar convertir numero_str en flotante
            el string recibido casteado a float -> si el string es un numero flotante positivo 
    '''
    numero_str = numero_str.strip()
    if(not (numero_str.replace('.','')).isdigit()):
        retorno = -1
    else:
        if(float(numero_str) < 0):
            retorno = -2
        else:
            try:
                numero = float(numero_str) 
                retorno = numero 
            except ValueError: 
                retorno = -3
    return retorno

#3.3
def sanitizar_string(valor_str, valor_por_defecto='-'):
    '''
    Analiza el string recibido y determina si es solo texto, sin numeros
    Parametros: numero_str:str -> un string que representa el texto a validar
                valor_por_defecto:str -> un string que representa un valor por defecto, inicializado con '-'
    Retorno: un string:
                'N/A' -> si el string contiene numeros
                valor_str convertido a minusculas -> si se verifica que es solo texto
                valor_por_defecto convertido a minusculas -> si el texto a validar es vacio               
    '''
    valor_str = valor_str.strip()
    valor_por_defecto = valor_por_defecto.strip()
    valor_str = valor_str.replace('/', ' ')
    if valor_str.isalpha():
        resultado =  valor_str.lower()
    else:
        if valor_str == '':
            resultado = valor_por_defecto.lower()
        else:
            resultado = 'N/A'
    return resultado

#3.4
def sanitizar_dato(heroe:dict,clave:str,tipo_dato:str)->bool:
    '''
    Sanitiza el valor del diccionario heroe correspondiente a la clave y al tipo de dato recibido.
    Parámetros:
        heroe (dict): El diccionario del héroe que contiene los datos a sanitizar.
        clave (str): La clave de los datos a sanitizar.
        tipo_dato (str): El tipo de dato a aplicar ('entero' para números enteros, 'flotante' para números con decimales, 'string' para texto).

    Retorna:
        bool: True si los datos se sanitizaron con éxito, False en caso contrario.
    '''
    se_sanitizo_dato = False
    clave = clave.lower()
    tipo_dato = tipo_dato.lower()
    if clave in heroe:
        if tipo_dato == 'entero':
            heroe[clave] = sanitizar_entero(heroe[clave])
            se_sanitizo_dato = True
        elif tipo_dato == 'flotante':
            heroe[clave] = sanitizar_flotante(heroe[clave])
            se_sanitizo_dato = True
        elif tipo_dato == 'string':
            heroe[clave] = sanitizar_string(heroe[clave])
            se_sanitizo_dato = True
        else:
            print("Tipo de dato no reconocido")
    else:
        print("La clave especificada no existe en el héroe.")
    return se_sanitizo_dato

#3.5
def stark_normalizar_datos(lista_heroes:list):
    '''
    Normaliza los datos en una lista de héroes según ciertos criterios.
    Parámetros:
        lista_heroes (list): La lista de héroes cuyos datos se normalizarán.

    Esta función normaliza los datos de altura, peso, color de ojos, color de pelo, fuerza e inteligencia en la lista de héroes.
    '''
    if len(lista_heroes) > 0:
        for heroe in lista_heroes:
            sanitizar_dato(heroe,'altura','flotante')
            sanitizar_dato(heroe,'peso','flotante')
            sanitizar_dato(heroe,'color_ojos','string')
            sanitizar_dato(heroe,'color_pelo','string')
            sanitizar_dato(heroe,'fuerza','entero')
            sanitizar_dato(heroe,'inteligencia','string')
    else:
        print("Error: Lista de héroes vacía.")

#4.1
def generar_indice_nombres(lista_heroes:list)->list:
    '''
    Genera un índice de nombres a partir de una lista de héroes.
    Parámetros: lista_heroes (list): La lista de héroes de la cual se generará el índice.
    Retorno: list: Una lista de nombres generados a partir de los nombres de los héroes.
    '''
    if(validar_lista(lista_heroes)):
        lista = []
        for heroe in lista_heroes:
            nombres = re.split("-| ",heroe['nombre'])
            for nombre in nombres:
                lista.append(nombre)
    else:
        print("El origen de datos no contiene formato correcto.")
    return lista

def stark_imprimir_indice_nombre(lista_heroes)->None:
    '''
    Imprime un índice de nombres a partir de una lista de héroes.
    Parámetros:
        lista_heroes: La lista de héroes de la cual se generará el índice y se imprimirá.
    '''
    indice = generar_indice_nombres(lista_heroes)
    print(('-').join(indice))

#5.1
def esta_entre(numero,un_numero,otro_numero)->bool:
    '''
    Verifica si un número está en el rango [un_numero, otro_numero].
    Parámetros: numero: El número a verificar.
                un_numero: El extremo inferior del rango.
                otro_numero: El extremo superior del rango.
    Retorna: un booleano -> True si el número está en el rango, False en caso contrario.
    """
    '''
    resultado = False
    if(numero > (un_numero - 1) and numero < (otro_numero + 1)):
        resultado = True
    return resultado

def generar_separador(patron:str,largo:int,imprimir=True):
    '''
    Genera un separador con un patrón especificado.
    Parámetros: patron (str): El patrón a utilizar para construir el separador.
                largo (int): La longitud del separador.
                imprimir (bool): Indica si se debe imprimir el separador (por defecto, True).
    Retorna:un string -> El separador generado.
    '''
    separador = ''
    if (esta_entre(len(patron),1,2) and (type(largo) == int) and esta_entre(largo,1,235)):
        for i in range(largo):
            separador += patron
        if imprimir:
            print(separador)
    else:
        separador = 'N/A'
    return separador
#5.2
def generar_encabezado(titulo:str):
    '''
    Genera un encabezado con un título especificado.
    Parámetros:  titulo (str): El título que se mostrará en el encabezado.
    Retorna: str: El encabezado generado.
    '''
    separador = generar_separador('*',120,False)
    titulo =  separador + '\n' + titulo.upper() + '\n' + separador +'\n'
    return titulo

#5.3 
def imprimir_ficha_heroe(heroe:dict)->None:
    '''
    Imprime una ficha detallada de un héroe.
    Parámetros:
        heroe (dict): El diccionario que contiene la información del héroe.
    """
    '''
    ficha = ''
    ficha += generar_encabezado('principal')
    ficha += f"\tNOMBRE DEL HÉROE:        {(obtener_nombre_con_iniciales(heroe)).replace('*','')}" +'\n'
    ficha += f"\tIDENTIDAD SECRETA:       {obtener_dato_formato(heroe['identidad'])}" +'\n' 
    ficha += f"\tCONSULTORA:              {obtener_dato_formato(heroe['empresa'])}" +'\n'
    ficha += f"\tCÓDIGO DE HÉROE:         {heroe['codigo_heroe']}" +'\n'
    ficha += generar_encabezado('fisico')
    ficha += f"\tALTURA:                  {heroe['altura']} cm." +'\n'
    ficha += f"\tPESO:                    {heroe['peso']} Kg." +'\n' 
    ficha += f"\tFUERZA:                  {heroe['fuerza']} N " +'\n'
    ficha += generar_encabezado('señas particulares') 
    ficha += f"\tCOLOR DE OJOS:           {heroe['color_ojos']}" +'\n'
    ficha += f"\tCOLOR DE PELO:           {heroe['color_pelo']}" +'\n'
    print(ficha)

#5.5 
def pedir_ingreso(opciones_validas:list):
    '''
    Pide al usuario que elija una opción de una lista de opciones válidas.
    Parámetros: opciones_validas (list): Una lista de opciones válidas.
    Retorna: un string -> La opción elegida por el usuario.
    '''
    ingreso = input("Elija una opcion: ")
    while ingreso not in opciones_validas:
        ingreso = input("Error. Elija una opcion valida: ")
    return ingreso

def mostrar_menu(menu:list)->None:
    '''
    Muestra un menú en la consola.
    Parámetros:  menu(list) Una lista de opciones que se mostrarán en el menú.
    '''
    for opcion in menu:
        print(opcion)

def obtener_ultimo_elemento(lista:list):
    '''
    Obtiene el último elemento de una lista.
    Parámetros: lista (list): La lista de la cual se obtendrá el último elemento.
    Retorna: El último elemento de la lista.
    '''
    return lista[len(lista) -1]


def stark_navegar_fichas(lista_heroes:list):
    '''
    Permite navegar por las fichas de héroes en una lista.
    Esta función muestra la ficha del héroe actual y permite al usuario navegar entre las fichas hacia la izquierda o la derecha.
    También proporciona la opción de volver al menú principal.

    Parámetros:  lista_heroes (list): La lista de héroes a través de la cual se navegará.
    '''
    seguir = True
    heroe_actual = lista_heroes[0]
    imprimir_ficha_heroe(heroe_actual)
    while seguir:
        mostrar_menu(['[1] Ir a la izquierda.','[2] Ir a la derecha.','[3] Volver al menú principal.'])
        opcion = pedir_ingreso(['1','2','3'])
        match opcion:
            case '1':
                if(heroe_actual == lista_heroes[0]):
                    heroe_actual = obtener_ultimo_elemento(lista_heroes)
                else:
                    indice_heroe_actual = lista_heroes.index(heroe_actual)
                    heroe_actual = lista_heroes[indice_heroe_actual - 1]
                imprimir_ficha_heroe(heroe_actual)
                pass
            case '2':
                if(heroe_actual == obtener_ultimo_elemento(lista_heroes)):
                    heroe_actual = lista_heroes[0]
                else:
                    indice_heroe_actual = lista_heroes.index(heroe_actual)
                    heroe_actual = lista_heroes[indice_heroe_actual + 1]
                imprimir_ficha_heroe(heroe_actual)
                pass
            case '3':
                seguir = False

def menu_principal(lista_personajes:list):
    '''
    Menú principal que permite al usuario interactuar con una lista de personajes.
    Esta función muestra un menú interactivo con varias opciones y permite al usuario realizar diferentes acciones en la lista de personajes.
    Parámetros:
        lista_personajes(list): Una lista que contiene información de personajes.
    '''
    seguir = True
    datos_normalizados = False
    se_generaron_codigos = False
    mensaje_error = 'ERROR. Primero se deben normalizar los datos.'
    menu = ['1- Imprimir la lista de nombres junto con sus iniciales.','2- Imprimir la lista de nombre y el código del mismo.','3- Normalizar datos.','4- Imprimir indice de nombres.','5- Navegar fichas.', '6- Salir.']
    while seguir:
        mostrar_menu(menu)
        opcion = pedir_ingreso(['1','2','3','4','5','6'])
        if(not datos_normalizados and opcion != '3' and opcion != 12):
            print(mensaje_error)
        else:  
            match opcion:
                case '1':
                    stark_imprimir_nombres_con_iniciales(lista_personajes)
                    pass
                case '2':
                    stark_generar_codigos_heroes(lista_personajes)
                    se_generaron_codigos = True
                    pass
                case '3':
                    if datos_normalizados:
                        print("Hubo un error al normalizar los datos. Verifique que la lista no esté vacía o que los datos ya no se hayan normalizado anteriormente") 
                    else:
                        stark_normalizar_datos(lista_personajes)
                        datos_normalizados= True
                        print('Datos normalizados.')
                    pass
                case '4':
                    stark_imprimir_indice_nombre(lista_personajes)
                    pass
                case '5':
                    if not se_generaron_codigos:
                        print("ERROR. Primero se deben generar los codigos (opcion 2)")
                    else:
                        stark_navegar_fichas(lista_personajes)
                    pass
                case '6':
                    seguir = False
menu_principal(lista_personajes)
        

