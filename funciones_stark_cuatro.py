import re
from data_stark import *

def extraer_iniciales(nombre_heroe):
    if len(nombre_heroe)!=0:
        nombre=re.sub('-', ' ', nombre_heroe)
        nombre=re.split(" ", nombre) #divide el nombre en items de lista por espacio
        iniciales=[inicial[0] for inicial in nombre if inicial.lower()!='the']#crea un diccionario donde toma el elemento inicial de cada palabra
        iniciales_str= '.'.join(iniciales) + '.' 
    else:
        iniciales_str= 'N/A'
    return iniciales_str  


def obtener_dato_formato(dato):
    if isinstance(dato,str) and len(dato)!=0:
        dato_pedido=re.sub(' ', '_', dato.lower())

    else:
        dato_pedido= False
    return dato_pedido


def stark_imprimir_nombre_con_iniciales(nombre_heroe):
    if isinstance(nombre_heroe,dict) and len(nombre_heroe['nombre'])!=0:
        nombre_pedido= obtener_dato_formato(nombre_heroe['nombre'])
        iniciales= extraer_iniciales(nombre_heroe['nombre'])
        resultado=f'*{nombre_pedido} ({iniciales})'
        
    else:
        resultado= False
    
    return resultado

def stark_imprimir_ide(ide_heroe):
    if isinstance(ide_heroe,dict) and len(ide_heroe['identidad'])!=0:
        nombre_pedido= obtener_dato_formato(ide_heroe['identidad'])
        
        
    else:
        nombre_pedido= False
    
    return nombre_pedido

def stark_imprimir_lista_con_iniciales(lista):
    if isinstance(lista,list) and len(lista)!=0:
        for element in lista:
            stark_imprimir_nombre_con_iniciales(element)
            return True
    else:
        return False




def generar_codigo_heroe(dict_heroe, id)->str:
    genero= dict_heroe['genero']
    codigo=0
    if len(genero)!=0 and (genero=='M' or genero=='F' or genero=='NB'):
        codigo_generado= genero.maketrans('MFNB','1200')
        codigo=genero.translate(codigo_generado)
        codigo=str(codigo)
        id=str(id)
        longitud=10-len(codigo)-len(genero)-1
        codigo= genero + '-' + codigo + id.zfill(longitud)        
    else:
        codigo='N/A'
    
    return codigo

def stark_generar_codigos_heroes(lista_heroes):
    id=1
    imprimir=''
    for e_stark in lista_heroes:
        codigo= generar_codigo_heroe(e_stark,id)
        id= id +1
        nombre= stark_imprimir_nombre_con_iniciales(e_stark)
        imprimir=  nombre + '||' + codigo
        print (imprimir)

def stark_generar_lista_inicial_heroes(lista_heroes):
    id=1
    imprimir=''
    for e_stark in lista_heroes:        
        id= id +1
        nombre= stark_imprimir_nombre_con_iniciales(e_stark)
        imprimir=  nombre 
        print (imprimir)
        



def sanitizar_entero(numero_entero:str):
    numero_entero=numero_entero.strip()
    if len(numero_entero)==0:
        numero=-3
    else:
        try:
            numero= float(numero_entero)
            if numero<0:
                numero=-2
        except ValueError:
            numero= -1 
    return numero

def sanitizar_flotante(numero_float:str):
    numero_float=numero_float.strip()
    if len(numero_float)==0:
        numero=-3
    else:
        try:
            numero= float(numero_float)
            if numero<0:
                numero=-2
        except ValueError:
            numero= -1  # Error: contiene caracteres no numéricos   
        

    return numero  # Devolver el número flotante positivo

def sanitizar_string(valor_str):
    
    for i in valor_str:
        if i!=" ":
            if i.isdigit():
                valor_str='N/A'
                break
    if valor_str!='N/A':
        if len(valor_str)==0:
            valor_str= '3'
        else:
            valor_str= valor_str.replace('/',' ')
        valor_str= valor_str.strip()
        valor_str= valor_str.lower()
    return valor_str


def sanitizar_dato(heroe, clave, tipo_dato):    
    sanitizar=False    
    if clave in heroe:
        if tipo_dato== 'entero':
            heroe[clave]= sanitizar_entero(heroe[clave])
        elif tipo_dato=='flotante':
            heroe[clave]= sanitizar_flotante(heroe[clave])
        elif tipo_dato=='string':
            heroe[clave]= sanitizar_string(heroe[clave])
        else:
            heroe[clave]= "tipo de dato no reconocido"        
        if heroe[clave]!='N/A':
            sanitizar= True
    else:
        print('La clave especificada no exist en el heroe')

    return sanitizar

def stark_normalizar_datos(lista_heroes):    
    if len(lista_heroes)!=0:
        lista_atributos= ['altura', 'peso', 'color_ojos','color_pelo','fuerza', 'inteligencia']
        for e in lista_heroes:           
            for i in lista_atributos:
                if i== 'altura' or i=='peso':
                    e[i]=sanitizar_dato(e, i, 'flotante' )
                elif i== 'color_ojos' or i=='color_pelo':
                    e[i]=sanitizar_dato(e, i, 'string' )
                elif i== 'fuerza'or i==  'inteligencia':
                    e[i]=sanitizar_dato(e, i, 'entero' )               
        print('DATOS NORMALIZADOS')
    else:
        print('ERROR: LISTA VACIA')


def stark_imprimir_indice_nombre(lista_heroes):
    mensaje= ""
    guion=""
    for e_stark in lista_heroes:
        nombre= e_stark['nombre']
        nombre= nombre.replace('the','')
        nombre= re.split(r'\s+', nombre)
        nombre_con_guion= '-'.join(nombre)        
        if e_stark!= lista_heroes[0]:
            guion='-'
        mensaje= mensaje +guion+ nombre_con_guion

    
    print(mensaje)



def generar_separador(patron, largo, imprimir:bool):
    separador=""
    if imprimir!=False:
        imprimir=True
    if imprimir== True:
        if len(patron)<=2 and largo>0 and largo<=255:
            for i in range(largo):
                separador= separador+patron
        else:
            separador= 'N/A'
    elif imprimir== False:
        separador=patron
    
    
    return separador



def generar_encabezado(titulo:str):
    separador= generar_separador('**', 20, True)
    encabezado= f'{separador}\n{titulo}\n{separador}'
    
    return encabezado

def imprimir_ficha_heroe(heroe:dict):
    encabezado_uno= generar_encabezado('PRINCIPAL')+ '\n'
    nombre= 'NOMBRE    ' + '            '+stark_imprimir_nombre_con_iniciales(heroe)+ '\n'
    identidad= 'IDENTIDAD' + '            '+stark_imprimir_ide(heroe)+ '\n'
    codigo='CODIGO   ' + '            '+generar_codigo_heroe(heroe,1)+ '\n'
    encabezado_dos= generar_encabezado('FISICO')+ '\n'
    altura='ALTURA' + '            '+heroe['altura']+ '\n'
    peso='PESO  ' + '            '+heroe['peso']+ '\n'
    fuerza='FUERZA' + '            '+heroe['fuerza']+ '\n'
    encabezado_tres= generar_encabezado('SEÑAS               PARTICULARES')+ '\n'
    color_ojos='COLOR DE OJOS' + '            '+heroe['color_ojos'].capitalize()+ '\n'
    color_pelo='COLOR DE PELO' + '            '+heroe['color_pelo'].capitalize()
    print(encabezado_uno, nombre,identidad, codigo, encabezado_dos, altura, peso, fuerza, encabezado_tres, color_ojos, color_pelo)


def stark_navegar_fichas(lista_heroes):
    
    i=0
    while True:
        opcion=input(('[ 1 ] Ir a la izquierda [ 2 ] Ir a la derecha [ 3 ] Salir: '))
        opcion=int(opcion)
        if opcion==1:
            i-=1
            print(imprimir_ficha_heroe(lista_heroes[i]))
        elif opcion==2:
            i+=1
            print(imprimir_ficha_heroe(lista_heroes[i]))
    
        elif opcion==3:
            print('saliendo....')
            break
        else:
            print('ingrese valor corrercto')


    
def stark_cuatro_app(lista_heroes):

    while True:
        print('1 - Imprimir la lista de nombres junto con sus iniciales\n')
        print('2 - Imprimir la lista de nombres y el código del mismo\n')
        print('3 - Normalizar datos\n')
        print('4 - Imprimir índice de nombres\n')
        print('5 - Navegar fichas\n')
        print('6 - Salir\n')
        opcion= input('Ingrese opcion: ')
        opcion= int(opcion)
        if opcion==1:
            stark_generar_lista_inicial_heroes(lista_heroes)

        elif opcion==2:
            stark_generar_codigos_heroes(lista_heroes)

        elif opcion==3:
            stark_normalizar_datos(lista_heroes)
            print('Datos sanitizados')

        elif opcion==4:
            stark_imprimir_indice_nombre(lista_heroes)

        elif opcion==5:
            stark_navegar_fichas(lista_heroes)

        elif opcion==6:
            print('Salir')
            break

stark_cuatro_app(lista_personajes)