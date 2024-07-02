# Funciones de conversión
def decimalToBinario(num):
    if (num == 0):
        return "0"
    binario = ""
    while num > 0:
        residuo = int(num % 2)
        num = int(num / 2)
        binario = str(residuo) + binario
    return binario
    
def decimalToOctal(num):
    if (num == 0):
        return "0"
    octal = ""
    while (num > 0):
        residuo = (num % 8) 
        num= int(num/8)
        octal= str(residuo) + octal
    return octal

def decimalToHexadecimal(num):
    if (num == 0):
        return "0"
    hexadecimal = "" 
    while num != 0: 
        rem = Cambiar(num % 16)
        num = int(num / 16)
        hexadecimal = str(rem) + hexadecimal
    return hexadecimal
def Cambiar(cambios):
    decimales = [10, 11, 12, 13, 14, 15]
    hexadecimal = ["A", "B", "C", "D", "E", "F"]
    for i in range(len(decimales)):
        if (cambios == decimales[i]):
            cambios = hexadecimal[i]
            break
    return cambios

def binarioToDecimal(binario):
    num = 0
    exp = 0
    while (binario > 0):
        cadena = binario%10
        binario = int(binario/10)
        num = num + cadena*pow(2, exp)
        exp = exp + 1
    return num

def octalToDecimal(octal):
    num = 0
    exp = 1
    while(octal):
        cadena = octal % 10
        octal = int(octal/10)
        num = num + cadena * exp
        exp = exp * 8
    return num

def octalToBinario(octal):
    if (octal == 0):
        return "0"
    binario = ""
    lista = []
    for i in range(len(octal)):
        if (octal[i]=='0'):
            lista.append('000')
        elif (octal[i]=='1'):
            lista.append('001')
        elif (octal[i]=='2'):
            lista.append('010')
        elif (octal[i]=='3'):
            lista.append('011')
        elif (octal[i]=='4'):
            lista.append('100')
        elif (octal[i]=='5'):
            lista.append('101')
        elif (octal[i]=='6'):
            lista.append('110')
        else:
            lista.append('111')
            
    for i in range (len(lista)):
        binario = binario + lista[i]

    return binario.lstrip("0")
def hexadecimalToBinario(hexadecimal):
    if (hexadecimal == 0):
        return "0"
    binario = ""
    lista=[]
    for i in range (len(hexadecimal)):
        if (hexadecimal[i]=='0'):
            lista.append('000')
        elif (hexadecimal[i]=='1'):
            lista.append('001')
        elif (hexadecimal[i]=='2'):
            lista.append('010')
        elif (hexadecimal[i]=='3'):
            lista.append('011')
        elif (hexadecimal[i]=='4'):
            lista.append('100')
        elif (hexadecimal[i]=='5'):
            lista.append('101')
        elif (hexadecimal[i]=='6'):
            lista.append('110')
        elif (hexadecimal[i]=='7'):
            lista.append('111')
        elif (hexadecimal[i]=='8'):
            lista.append('1000')
        elif (hexadecimal[i]=='9'):
            lista.append('1001')
        elif (hexadecimal[i]=='A' or hexadecimal[i]=='a'):
            lista.append('1010')
        elif (hexadecimal[i]=='B' or hexadecimal[i]=='b'):
            lista.append('1011')
        elif (hexadecimal[i]=='C' or hexadecimal[i]=='c'):
            lista.append('1100')
        elif (hexadecimal[i]=='D' or hexadecimal[i]=='d'):
            lista.append('1101')
        elif (hexadecimal[i]=='E' or hexadecimal[i]=='e'):
            lista.append('1110')
        elif (hexadecimal[i]=='F' or hexadecimal[i]=='f'):
            lista.append('1111')
        else:
            binario = 1 # REVISAR VALIDACION
            break

    if (binario == ""):
        for i in range (len(lista)):
            binario = binario + lista[i]
        return binario
    else:
        print("error, vuelva a escribir")
        
## Validaciones
def es_binario(numero):
    numero_str = str(numero)
    for digito in numero_str:
        if digito not in ['0', '1']:
            return False
    return True
def es_octal(numero):
    numero_str = str(numero)
    for digito in numero_str:
        if digito not in ['0', '1', '2', '3', '4', '5', '6', '7']:
            return False
    return True

def menu():
    menuconv = '''            
            //////////////////////////////////////////////////
            ///                                            ///
            ///    MENÚ CONVERSIÓN DE SISTEMAS NUMÉRICOS   ///
            ///                                            ///
            ///          1) Entero -> Binario              /// 1
            ///          2) Entero -> Octal                /// 1 
            ///          3) Entero -> Hexadecimal          /// 1
            ///          4) Binario -> Entero              /// 1
            ///          5) Octal -> Entero                /// 1
            ///          6) Octal -> Binario               /// 1
            ///          7) Octal -> Hexadecimal           /// 1_
            ///          8) Hexadecimal -> Entero          /// 1_
            ///          9) Hexadecimal -> Binario         /// 1
            ///         10) Hexadecimal -> Octal           /// 1_
            ///          0) Cerrar / Salir                 ///
            ///                                            ///                    
            //////////////////////////////////////////////////
            
            Ingrese una opción del menú: '''                  
        
    opcion = ''
    while(opcion != 0):
        opcion = int(input(menuconv))

        if (opcion == 1):
            num = int(input("Ingrese un número Entero: "))
            binario = decimalToBinario(num)
            print (f'el numero decimal: {num} en binario es: {[binario]}')

        elif (opcion == 2):
            num = int(input("Ingrese un número Entero: "))
            octal = decimalToOctal(num)
            print (f'el numero decimal: {num} en octal es: {[octal]}')

        elif (opcion == 3):
            num = int(input("Ingrese un numero positivo para convertirlo a hexadecimal: "))
            hexadecimal = decimalToHexadecimal(num)
            print (f'el numero decimal: {num} en hexadecimal es: {[hexadecimal]}') 
            
        elif (opcion == 4):
            num = int(input("Ingresa un número binario: "))
            if es_binario(num):
                decimal = binarioToDecimal(num)
                print (f'el numero binario: {num} en decimal es: {[decimal]}')
            else:
                print(f'el numero {num} no es binario.')

        elif (opcion == 5):
            num = int(input("Ingrese un numero octal: "))
            if es_octal(num):
                decimal = octalToDecimal(num)
                print (f'el numero octal: {num} en decimal es: {[decimal]}')
            else:
                print(f'el numero {num} no es octal.')
        
        elif (opcion == 6):
            num = str(input("Ingrese un número octal: "))
            if es_octal(num):
                binario = octalToBinario(num)
                print (f'el numero octal: {num} en binario es: {[binario]}')
            else:
                print(f'el numero {num} no es octal.')
        
        elif (opcion == 7):
            num = int(input("Ingrese un número octal: "))
            if es_octal(num):
                hexadecimal = decimalToHexadecimal(octalToDecimal(num))
                #CREAR FUNCIÓN PROPIA PENDIENTE octalToHexadecimal(num)
                print (f'el numero octal: {num} en hexadecimal es: {[hexadecimal]}')
            else:
                print(f'el numero {num} no es octal.')
        #MEJORAR
        elif (opcion == 8):
            num = int(input("Ingrese un número hexadecimal: "))
            decimal = binarioToDecimal(hexadecimalToBinario(num))
            print (f'el numero hexadecimal: {num} en decimal es: {[decimal]}')
        elif (opcion == 9):
            num = str(input("Ingrese un número hexadecimal: "))
            binario = hexadecimalToBinario(num)
            print (f'el numero hexadecimal: {num} en binario es: {[binario]}')
   
            def hexa_binario():
                z=0
                list=[]
                hexa=str(input("ingrese hexadecimal (letras en mayúscula): "))
                contador=0
                for contador in range (len(hexa)):
                    if hexa[contador]=='0':
                        list.append('0')
                    elif hexa[contador]=='1':
                        list.append('1')
                    elif hexa[contador]=='2':
                        list.append('10')
                    elif hexa[contador]=='3':
                        list.append('11')
                    elif hexa[contador]=='4':
                        list.append('100')
                    elif hexa[contador]=='5':
                        list.append('101')
                    elif hexa[contador]=='6':
                        list.append('110')
                    elif hexa[contador]=='7':
                        list.append('111')
                    elif hexa[contador]=='8':
                        list.append('1000')
                    elif hexa[contador]=='9':
                        list.append('1001')
                    elif hexa[contador]=='A':
                        list.append('1010')
                    elif hexa[contador]=='B':
                        list.append('1011')
                    elif hexa[contador]=='C':
                        list.append('1100')
                    elif hexa[contador]=='D':
                        list.append('1101')
                    elif hexa[contador]=='E':
                        list.append('1110')
                    elif hexa[contador]=='F':
                        list.append('1111')
                    else:
                        z=1
                        break
                    contador+=1
                if z==0:
                    for i in range (len(list)):
                        print(list[i])
                else:
                    print("error, vuelva a escribir")
                    
            hexa_binario()
        elif (opcion == 10):
            num = int(input("Ingrese un número hexadecimal: "))
            octal = decimalToOctal(binarioToDecimal(hexadecimalToBinario(num)))
            print (f'el numero hexadecimal: {num} en octal es: {[octal]}')

        elif opcion == 0: print("!Has salido del menu!")
        else: print ("OPCIÓN NO ENCONTRADA, por favor digite una de las opciones del menu.")          

menu()