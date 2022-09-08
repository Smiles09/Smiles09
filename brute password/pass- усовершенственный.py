import numbers
import random

login =input()
name = input()
surname =input()
birth_data =input()
birth_month =input()
birth_year =input()


combinations = [ name, surname, birth_data, birth_month, birth_year, login, '_', '.',str(1),str(2),str(3),str(4),str(5),str(6),str(7),str(8),str(9),str(0)]

number = int( input ( 'КОЛИЧЕСТВО ПАРОЛЕЙ:') )
lenght =int ( input( 'длина строки:') )

for x in range ( number ):
	password = ''
	
	for i in range ( lenght ):
		password += random.choice ( combinations )
	
	print ( password )

	file = open('password.txt', 'a')
	file.write('\n'+ password)
	file.close()
