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
    while(binario > 0):
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
            ///          6) Octal -> Binario               /// 0
            ///          7) Octal -> Hexadecimal           /// 0
            ///          8) Hexadecimal -> Entero          /// 0
            ///          9) Hexadecimal -> Binario         /// 0
            ///         10) Hexadecimal -> Octal           /// 0
            ///          0) Cerrar / Salir                 ///
            ///                                            ///                    
            //////////////////////////////////////////////////
            
            Ingrese una opción del menú: '''                  
        
    opcion = ''
    while(opcion != 0):
        opcion = int(input(menuconv))

        if (opcion == 1):
            num = int(input("Ingrese un número decimal: "))
            binario = decimalToBinario(num)
            print (f'el numero decimal: {num} en binario es: {[binario]}')

        elif (opcion == 2):
            num = int(input("Ingrese un número decimal: "))
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

        elif opcion == 8: #Conversión hexadecimal – decimal
            def obtener_valor_real(cambios_hexadecimal):
                cambios = {
                    "f": 15,
                    "e": 14,
                    "d": 13,
                    "c": 12,
                    "b": 11,
                    "a": 10,
                }
                if cambios_hexadecimal in cambios:
                    return cambios[cambios_hexadecimal]
                else:
                    return int(cambios_hexadecimal)
            def hexadecimal_decimal(hexadecimal):
                hexadecimal = hexadecimal.lower()
                hexadecimal = hexadecimal[::-1]
                decimal = 0
                posicion = 0
                for cambiar in hexadecimal:
                    valor = obtener_valor_real(cambiar)
                    elevado = 16 ** posicion
                    equivalencia = elevado * valor
                    decimal += equivalencia
                    posicion += 1
                return decimal
            hexadecimal = input("Ingresa un número hexadecimal: ")
            decimal = hexadecimal_decimal(hexadecimal)
            print(f"El hexadecimal {hexadecimal} es {decimal} en decimal")

        elif opcion == 7: #Conversión octal – hexadecimal
            num = int(input("Ingrese un número octal:   "))
            exp = 0
            i = 0
            decnum = 0
            while num!=0:
                rem = num%10
                print(rem)
                if rem>7:
                    exp = 1
                    break
                decnum = decnum + (rem * (8 ** i))
                i = i+1
                num = int(num/10)
            if exp == 0:
                i = 0
                hexdecnum = []
                while decnum != 0:
                    rem = decnum % 16
                    if rem < 10:
                        rem = rem + 48
                    else:
                        rem = rem + 55
                    rem = chr(rem)
                    hexdecnum.insert(i, rem)
                    i = i + 1
                    decnum = int(decnum / 16)
                print("El octal ingresado en hexadecimal es:   ")
                i = i - 1
                while i >= 0:
                    print(end=hexdecnum[i])
                    i = i - 1
            else:
                print(f'el numero {num} no es octal')
        
        elif opcion == 10: #Conversión hexadecimal – octal
            hexa = str(input("ingrese número hexadecimal (letras en Mayúscula): "))
            exp = 0
            num = 0
            hexad = len(hexa)
            hexad = hexad-1
            i = 0
            while hexad>=0:
                rem = hexa[hexad]
                if rem>='0' and rem<='9':
                    rem = int(rem)
                elif rem>='A' and rem<='F':
                    rem = ord(rem)
                    rem = rem-55
                elif rem>='a' and rem<='f':
                    rem = ord(rem)
                    rem = rem-87
                else:
                    exp = 1
                    break
                num = num + (rem * (16 ** i))
                hexad = hexad-1
                i = i+1
            if exp==0:
                i = 0
                octnum = []
                while num!=0:
                    rem = num%8
                    octnum.insert(i, rem)
                    i = i+1
                    num = int(num/8)
                print("El hexadecimal ingresado en octal es: ")
                i = i-1
                while i>=0:
                    print(octnum[i], end="")
                    i = i-1
                print()
            else:
                print(f"el numero {hexa} no es hexadecimal!")
        
        elif opcion == 9: #Conversión hexadecimal – binario
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

        elif opcion == 6: #Conversión octal - binario
            def octal_binario():
                z=0
                list=[]
                hexa=str(input("ingrese octal:  "))
                contador=0
                for contador in range (len(hexa)):
                    if hexa[contador]=='0':
                        list.append('000')
                    elif hexa[contador]=='1':
                        list.append('001')
                    elif hexa[contador]=='2':
                        list.append('010')
                    elif hexa[contador]=='3':
                        list.append('011')
                    elif hexa[contador]=='4':
                        list.append('100')
                    elif hexa[contador]=='5':
                        list.append('101')
                    elif hexa[contador]=='6':
                        list.append('110')
                    elif hexa[contador]=='7':
                        list.append('111')
                    else:
                        z=1
                        break
                    contador+=1
                if z==0:
                    for i in range (len(list)):
                        print(list[i])
                else:
                    print(f"error {hexa} no es octal, vuelva a escribir")
            octal_binario()
        
        elif opcion == 0: print("Ha salido del menu!")
        else: print ("OPCIÓN NO ENCONTRADA, por favor digite una de las opciones del menu")          

menu()

