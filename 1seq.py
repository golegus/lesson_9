list_len=input('Введите количество элементов списка: ')
if not list_len.isdigit():
    print('Количество элементов должно выражаться в целочисленном виде') 
    raise SystemExit(1)

list_len=int(list_len)
my_list=[]

for item in range(list_len):
    while True:
        val=input(f'Введите {item+1} элемент: ')
        if val.isdigit():
            my_list.append(int(val))
            break
        else:
            print('Элементами списка могут быть только целочисленные значения!')
        
print(my_list)
