fruits={"apple":"red", "mango": "yellow", "blueberry":"blue", "orange": "orange", "kiwi":"green", "banana": "yellow", "watermelon": "red", "musk melon": "yellow"}

list1=list(fruits.keys())
colours=list(fruits.values())
print(fruits.items())
print(colours)
print(list1)

for i in fruits:
    print(i)

count=0
clr=input("Enter a colour: ")
for i in fruits.values():
    if i==clr:
        count+=1

print(f'{clr} colour fruits is present {count} times')
b=0
for i in fruits.keys():
    if i[0]=='b':
        b+=1

print(f'fruits names sterting with b is {b}')