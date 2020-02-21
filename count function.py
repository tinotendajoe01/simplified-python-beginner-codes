

def count(list):
    even_numbs = 0
    odd_numbs = 0
    for i in list:
        if i % 2 == 0:
            even_numbs += 1
        else:
            odd_numbs +=1
    return even_numbs, odd_numbs
list= []
length = int(input("enter the list length: "))
print("enter numbers: ")
for i in range (length):
    data= int(input())
    list.append(data)
print(list)

even_numbs, odd_numbs = count(list)
print("even numbers: {}".format(even_numbs, odd_numbs))
print("odd numbers: {}".format(odd_numbs, even_numbs))