# ipsum_file = open('./files/ipsum.txt')
# # for line in ipsum_file:
# #     print(line.rstrip())

# # ipsum_file.seek(0)
# # print(ipsum_file.readlines())

# #reading from a particular line

# # ipsum_file.seek(20)

# # print(ipsum_file.read(400))

# # ipsum_file.close()

# using automatic opener and close

with open('./files/ipsum.txt') as text:
    print(text.readlines())
