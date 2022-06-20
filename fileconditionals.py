filen = input("Please enter a filename." )

type = filen.split('.')[1].lstrip().split(' ')[0]
print(type)