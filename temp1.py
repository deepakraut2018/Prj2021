
my_file = open('Temp.txt')

print(my_file.read())
my_file.seek(0)
print(my_file.readline())
print(my_file.readline())
#print(my_file.readline())