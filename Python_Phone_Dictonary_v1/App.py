my_dict = {}


def rec(my_data, per, phone):
	my_data[per] = phone


def person():
	name = input('> Enter your Name: ')
	phone = input('> Enter your Phone number: ')
	rec(my_dict, name, phone)


def modify(name):
	num = input(f'\n> Enter the changed number for {name} : ')
	my_dict[name] = num

	print(f'\n> changed-> {name} : {my_dict[name]}')


def search(name):
	if name not in my_dict:
		print('\nPerson not found')
	else:
		print(f'{name} : {my_dict[name]}')


for i in range(int(input('> no of loops: '))):
	op = int(input('\n> Enter your choice \n1.Enter new person \n2.Modify Data \n3.Search For person \n: '))

	if op == 1:
		person()

	elif op == 2:
		nam = input('\n> Enter The name to change: ')
		modify(nam)

	elif op == 3:
		sch = input('> Enter the name to search: ')
		search(sch)

	else:
		print('\nThis is an invalid option.')
