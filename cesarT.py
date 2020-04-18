alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
alfabeto2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def codificar(cadena, desplazamiento):
	cifrado = ""

	for letra in cadena: #Revisamos cada letra de la cadena ingresada
		if letra.upper() in alfabeto:
			temp = ""
			x = alfabeto.find(letra.upper())#regresa el indice de la i-esima letra de la cadena en el alfabaeto
			l_c = (x + desplazamiento) % len(alfabeto)#se obtiene el nuevo indice ya con el corrimiento
			temp = alfabeto[l_c]
			cifrado += temp
		else:
			cifrado += letra# se pasa la letra igual puessto que no esta en el alfabeto

	return cifrado.lower()

def descifrado(cadena, desplazamiento):
	descifrado = ""
	for letra in cadena:
		if letra.upper() in alfabeto:
			y = alfabeto.find(letra.upper())
			l_d = (y - desplazamiento) % len(alfabeto)
			temp = alfabeto[l_d]
			descifrado += temp
		else:
			descifrado += letra

	return descifrado.lower()


def codificar2(cadena, desplazamiento):
	cifrado = ""

	for letra in cadena: #Revisamos cada letra de la cadena ingresada
		if letra.upper() in alfabeto2:
			temp = ""
			x = alfabeto2.find(letra.upper())#regresa el indice de la i-esima letra de la cadena en el alfabaeto
			l_c = (x + desplazamiento) % len(alfabeto2)#se obtiene el nuevo indice ya con el corrimiento
			temp = alfabeto2[l_c]
			cifrado += temp
		else:
			cifrado += letra# se pasa la letra igual puessto que no esta en el alfabeto

	return cifrado.lower()

def descifrado2(cadena, desplazamiento):
	descifrado = ""
	for letra in cadena:
		if letra.upper() in alfabeto2:
			y = alfabeto2.find(letra.upper())
			l_d = (y - desplazamiento) % len(alfabeto2)
			temp = alfabeto2[l_d]
			descifrado += temp
		else:
			descifrado += letra

	return descifrado.lower()


with open("ejercicio4.txt") as cifrado:
	mensaje = cifrado.read()

print(mensaje)


#este with creara el archivo res_ejer4.txt
with open("res_ejer4.txt", "w") as f:
	f.write(descifrado2(mensaje,11))



##################Prueba para obtener el cifrado##########################

# mensaje = "szwl xfnslnszd"
# for i in range(0,len(alfabeto)):
# 	print("Corrida numero " + str(i))
# 	print("decodificado 1 " + descifrado(mensaje,i))
# 	print("decodificado 2 " + descifrado2(mensaje,i) +"\n")







