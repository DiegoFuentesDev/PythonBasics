text = open('./PythonBasics/PythonBasics/filetxt.txt', 'w')

text.write("\nAdding a NEW LINE!!!!!!!!!!!!")

# for index in text:
#     print(index)

text.close()

text = open('./PythonBasics/PythonBasics/filetxt.txt')

print(text.read())

# import os

# if os.path.exists('./PythonBasics/PythonBasics/filetxt.txt'):
#     os.remove('./PythonBasics/PythonBasics/filetxt.txt')
# else:
#     print('File does not exist')