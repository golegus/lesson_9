num_list=input('Введите несколько цифр через запяту, слэш или точку с запятой. \nМожно использовать только один тип разделителя. \nВвод: ')
seps=[',',';','/']
my_separator=''
for sep in seps:
    if sep in num_list and my_separator!='':
        print('Ошибка! Можно использовать только один тип разделителя!')
        raise SystemExit(1)
    elif sep in num_list:
        my_separator=sep      

num_set=set(num_list.split(my_separator))
print(', '.join(num_set))
