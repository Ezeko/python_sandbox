#this is comment in python

#name = input('Tell me your name: ')

#print('welcome ' + name)

# radius = input('What is the Radius of the circle?')

# area = (22/7) * (int(radius) ** 2)

# print('The area of the circle with radius:', radius, '=',area)

# num1 = [90,78, 9, 13, 78, 9, 12]
# num2 = [87, 7, 8, 9, 19, 0]
# # del(num1[2])
# # print(num1)

# print ('first number is {0}, second number is {1}'.format(num1,num2))

# print(f'first {num1}, second {num2} ')

# age = input('Tell me your age:')

# if int(age) < 18 :
#     print(f'😳pps! You have {18 - int(age)} years to be eligible to drive')

# elif int (age) >= 18 :
#     print('You are eligible to drive 👍🏼')
# else :
#     print('Kindly input a valid age')

# loops

# for loops

students = ['ade', 'olu', 'ola', 'ope', 'olawale', 'eze', 'joseph']

# for student in students :
#     print (student)

#while loops

# count = 0
# # while count < len(students): 
# #     print(students[count])
# #     count +=1

# while count < 25 :
#     if count < 1 :
#         count +=1
#         continue
#     if count % 2 == 0 :
#         print (count)
#     count +=1

#range


# for n in range(1,9,2):
#     print(n)

# print(sorted(students))

def sayName(name) :
    print(f'your name is {name}')


name = input('Tell me your name: ')

sayName(name)
while True:
    ask = input('continue? y/n: ')
    if ask == 'y':
        name = input('Any other name: ')
        sayName(name)
        continue
    elif ask == 'n':
        break
    else:
        print('Reply with either \'y\' or \'n\' ')
        continue