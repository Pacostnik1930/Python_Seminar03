list = [1,2,3,4,5]

k = int(input('Введите сдвиг:'))

new_List = []
for i in range (k):
    new_List.insert(0,list[len(list) - 1 - i])

for i in range(len(list)- k):
    new_List.append(list[i])
    print(new_List)