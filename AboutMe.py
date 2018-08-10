from datetime import datetime

print('Hello!')
print('''
That's my dog

O____
 ||||`

I Live In Dhaka and I like songs

╔══╗ 
║██║ 
║(O)║♫ ♪ ♫ ♪
╚══╝
''')

birth_year = input("I can tell your age. Say me your birth year :)\n")
age = datetime.now().year - int(birth_year)

print("Your age is", age)
print("If you were a dog, you'd be", age * 7, "!!")
print("Ha " * 3)
