import sys
from pyparsing import *

def delComment(text):
    new_text = ''
    # удаление комментов
    begin = 0
    end = text.find("//") # находим в тексте "struct"
    while end != -1:
        new_text += text[begin: end]
        begin = end
        # находим конец блока
        begin = text.find('\n', begin)  
        end = text.find("//", begin+1) 
    return new_text 

# читаем файл: lines -- список, каждый элемент которого содержит отдельную строку файла 
f = open('vDocMsg.h')
text = f.read()
f.close()    




structs = []
struct = ''


# парсим на структуры
end = text.find("struct") # находим в тексте "struct"
# заполняем лист фигур
while end != -1:
    begin = end
    # находим конец блока
    end   = text.find('};', begin)
    # добавляем блок в список структур
    structs.append(text[begin: end])    
    end = text.find("struct", end)  

# вывод строк
count = 0
for line in structs:
    count += 1
    print(line)
    if count > 100: 
        break