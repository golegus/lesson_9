num_list1=input('Cписок 1.\nВведите несколько цифр через запятую. \nВвод: ')
num_list1 = num_list1.split(',')

num_list2=input('Cписок 2.\nВведите несколько цифр через запятую. \nВвод: ')
num_list2 = num_list2.split(',')

for i in num_list2:
    for val in num_list1:
       if i in num_list1:
            num_list1.remove(i)

print(', '.join(num_list1))

