##sup=[1,2,3,4,5,6]
#suma = sup[3] + sup[4]
#print(suma)
#print('nombre de tu gato')
#cat=input()
#print('el nombre de tu gato es ' + cat)
ACTANO=2023
print('1. ¿Cuál es tu nombre?') 
nombre=input()
print('2. ¿Cuál es tu primer apellido?') 
apellido=input()
print('3. ¿Cuál es tu segundo apellido?') 
segapellido = input()
print('4. ¿En qué año naciste?') 
ano=input()
inano = int(ano)
print('5. ¿En qué mes y día naciste? (en el siguiente formato “mm-dd”)') 
md=input()
BD= md[-2:] + '-' + md[0:2] + '-' + ano 
edad = ACTANO - inano
stedad=str(edad)

lowername= nombre.lower() + apellido.lower() + segapellido.lower()
vowellist= ['a','e','i','o','u']
count_v = 0
for word in lowername:
    #print(word)
    if word in vowellist:
    	count_v = count_v + 1
print(count_v)

isnum = isinstance(edad,int)
isstr = isinstance(lowername,str)
edad10 = edad + 10
edad20= edad +20
edadmed=  round((edad + edad20)/2)

print('A. Este es tu nombre completo en mayúsculas ' + nombre.upper() + " " +apellido.upper())
print('B. Este es tu nombre completo en minúsculas ' + nombre.lower() + " " +apellido.lower())
print('C. Esta es tu fecha de nacimiento ' + BD)
print('D. Esta es tu edad ' + stedad)
print('E. Tu nombre completo tiene ' + str(count_v) +' vocales.')
print('F. Tu nombre completo tiene ' + str(len(lowername)) + ' letras.')
print('G. ¿Tu edad es un carácter de tipo número? ' + str(isnum))
print('H. ¿Tu nombre completo es un carácter de tipo alfanumérico? ' + str(isstr))
print('I. Tu edad en 10 años será ' + str(edad10))
print('J. La media de tu edad actual y tu edad en 20 años es ' + str(edadmed))