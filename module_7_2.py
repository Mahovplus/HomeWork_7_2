def custom_write(file_name, *strings):
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    for string in strings:                     #Пакуем информацию по строкам в файл
        file.write(f"{string}\n")
    file.close()
    file = open(file_name, 'r', encoding='utf-8')
    count = 0
    while  count < 4:
        byte = file.tell()
        line = file.readline()
        lines = line.replace('\n', '')
        count += 1
        strings_positions.setdefault((count, byte), lines)
    file.close()
    return  strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', *info)
print(result)
for elem in result.values():
  print(elem)
#print(linecache.getline('test.txt', 2))
#for number, string in enumerate(git):
#    git_2 = print(f'{number} {string}')
#    strings_positions.update()
#file.close()
#byte = len(string.encode('utf-8'))
