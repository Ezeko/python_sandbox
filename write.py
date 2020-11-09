# writing in file 
with open('./files/newwrite.txt', 'w') as file:
    file.write('bla bla bla')


# adding to file 

## using 'a' will add to existing file

with open('./files/newwrite.txt', 'a') as file:
    file.write('\nAnother stuff added with python')