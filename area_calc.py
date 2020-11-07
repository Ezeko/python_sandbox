# #this is comment in python

# #name = input('Tell me your name: ')

# #print('welcome ' + name)

# # radius = input('What is the Radius of the circle?')

# # area = (22/7) * (int(radius) ** 2)

# # print('The area of the circle with radius:', radius, '=',area)

# # num1 = [90,78, 9, 13, 78, 9, 12]
# # num2 = [87, 7, 8, 9, 19, 0]
# # # del(num1[2])
# # # print(num1)

# # print ('first number is {0}, second number is {1}'.format(num1,num2))

# # print(f'first {num1}, second {num2} ')

# # age = input('Tell me your age:')

# # if int(age) < 18 :
# #     print(f'😳pps! You have {18 - int(age)} years to be eligible to drive')

# # elif int (age) >= 18 :
# #     print('You are eligible to drive 👍🏼')
# # else :
# #     print('Kindly input a valid age')

# # loops

# # for loops

# students = ['ade', 'olu', 'ola', 'ope', 'olawale', 'eze', 'joseph']

# # for student in students :
# #     print (student)

# #while loops

# # count = 0
# # # while count < len(students): 
# # #     print(students[count])
# # #     count +=1

# # while count < 25 :
# #     if count < 1 :
# #         count +=1
# #         continue
# #     if count % 2 == 0 :
# #         print (count)
# #     count +=1

# #range


# # for n in range(1,9,2):
# #     print(n)

# # print(sorted(students))


# ### Functions
# # def sayName(name) :
# #     print(f'your name is {name}')


# # name = input('Tell me your name: ')

# # sayName(name)
# # while True:
# #     ask = input('continue? y/n: ')
# #     if ask == 'y':
# #         name = input('Any other name: ')
# #         sayName(name)
# #         continue
# #     elif ask == 'n':
# #         break
# #     else:
# #         print('Reply with either \'y\' or \'n\' ')
# #         continue


# ##class

# # class Person():
# #     def __init__(self):
# #         self.name = 'Ezeko'
# #         self.age = 19
# #         self.occupation = 'Software Development'
        
# # myself = Person()

# # print(f'my name is {myself.name}, I am {myself.age} years old')


# ## using init

# # class InitClass():
# #     def __init__(self, name, age, occupation, department):
# #         self.name = name
# #         self.age = age
# #         self.occupation = occupation
# #         self.department = department

# # wale = InitClass('Olawale', 17, 'Teaching', 'Programming')
# # print(f'Hello there, my name is {wale.name}, I am {wale.age} years old') 

# # biola = InitClass('Abiola', 27, 'Accounting', 'Forensic')
# # print(f'Hello there, my name is {biola.name}, I am {biola.age} years old')

# ## class method

# # class ClassMethodTest():
    
# #     globalVariable = 'something accessible any where in the class'
    
# #     @classmethod
# #     def clmthd(cls):
# #         return ('this is a class method')
    
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
    

# # print(ClassMethodTest.globalVariable)


# # nerw = ClassMethodTest('Biola', 87)

# # # print (f'{nerw.globalVariable} accessed from {nerw.name}')

# # print(f'{ClassMethodTest.clmthd()}')

# ## List comprehension

# prizes = [80, 50, 67, 9, 56, 9, 77]

# double_prizes = [prize * 2 for prize in prizes]

# print (double_prizes)


# ##squaring numbers

# numbers = [1,2,3,4,5,6,7,8,9,10]

# square_num = [number ** 2  for number in numbers if number % 2 == 0]

# print(f'squared {numbers} is {square_num}')

#DECORATORS

def decoTest(func):
    #do this before passed func
    print('This is before the function')
    print('--------------------------')
    func()
    print('--------------------------')
    print('This is after function')
    

@decoTest
def someFunc():
    return print('THIS is the function itself')

    