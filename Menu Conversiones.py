def menu():
    menuconv = '''            //////////////////////////////////////////////////
            ///    MENÚ CONVERSIÓN DE SISTEMAS NUMÉRICOS   ///
            ///                                            ///
            ///     1. Conversión decimal a binario        ///           
            ///     2. Conversión binario a decimal        ///
            ///     3. Conversión decimal a octal          ///
            ///     4. Conversión octal a decimal          ///
            ///     5. Conversión decimal a hexadecimal    ///
            ///     6. Conversión hexadecimal a decimal    ///
            ///     7. Conversión octal a hexadecimal      ///
            ///     8. Conversión hexadecimal a octal      ///
            ///     9. Conversión hexadecimal a binario    ///
            ///    10. Conversión octal a binario          ///
            ///    11. Cerrar/Salir                        ///                    
            //////////////////////////////////////////////////
            
            Digite una opción < 1 - 11 >:'''                  
        
    opcion = 0
    while(opcion != 11):
        opcion = int(input(menuconv))

        if opcion == 1: #Conversión decimal – binario
            num = int(input("Ingresa un número decimal: "))
            def deci_bina(num):
                if num ==0:
                    return "0"
                binario = ""
                while num >=1:
                    residuo = int(num % 2)
                    num = int(num / 2)
                    binario = str(residuo) + binario
                return binario
            binario = deci_bina(num)
            lista=[binario]
            print (f'el numero decimal: {num} en binario es: {lista}')
            
        elif opcion == 2: #Conversión binario – decimal
            binario = int(input("ingrese un numero binario: "))
            def bina_deci(binario):
                num=0
                exp=0
                while(binario>=1):
                    cadena=binario%10
                    binario=int(binario/10)
                    num = num + cadena*pow(2, exp)
                    exp = exp + 1
                print(f'el binario ingresado en numero decimal es: {[num]}')
            bina_deci(binario)

        elif opcion == 3: #Conversión decimal – octal
            num = int (input("Ingresa un número decimal: "))
            def deci_oct(num):
                if (num ==0 ):
                    return "0"
                octal = ""
                while num >0:
                    residuo = num%8
                    octal=str(residuo)+ octal
                    num= int (num/8)
                return octal
            octal = deci_oct(num)
            print (f'el numero: {num} en octal es: {[octal]}')

        elif opcion == 4: #Convertir octal - decimal
            num = int(input("ingrese un numero octal: "))
            def octal_deci(num):
                deci = 0
                exp = 1
                l=[]
                def string_int(data): 
                    for i in str(data):
                        l.append(int(i))
                string_int(num)
                if (8 in l) or (9 in l):
                    return f'NO VALIDO, EL NUMERO {num} NO ES OCTAL'
                else:
                    while(num):
                        cadena = num % 10
                        num = int(num/10)
                        deci = deci+ cadena * exp
                        exp = exp *8
                    return deci
            print(f'el octal {num} en decimal es: {octal_deci(num)}')
            
        elif opcion == 5: #Conversión decimal – hexadecimal
            def DecimalAHexadecimal(): 
                decimal = int(input("Introduzca un numero positivo para convertirlo a hexadecimal: ")) 
                hexadecimal = "" 
                while decimal != 0: 
                    rem = Cambiar(decimal % 16)
                    hexadecimal = str(rem) + hexadecimal
                    decimal = int(decimal / 16)
                print("El resultado en hexadecimal es: " + hexadecimal) 
            def Cambiar(cambios):
                decimales =     [10 , 11 , 12 , 13 , 14 , 15 ]
                hexadecimal = ["A", "B", "C", "D", "E", "F"]
                for c in range(7):
                    if cambios == decimales[c - 1]:
                        cambios = hexadecimal[c - 1]
                return cambios
            DecimalAHexadecimal()

        elif opcion == 6: #Conversión hexadecimal – decimal
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
        
        elif opcion == 8: #Conversión hexadecimal – octal
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

        elif opcion == 10: #Conversión octal - binario
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
        
        elif opcion == 11: print("Ha salido del menu!")
        else: print ("OPCIÓN NO ENCONTRADA, por favor digite una de las opciones del menu")          

menu()