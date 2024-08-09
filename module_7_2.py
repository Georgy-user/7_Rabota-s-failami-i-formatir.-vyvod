def custom_write(file_name, strings):
    nf = open(file_name, 'w', encoding='utf-8')
    string_positions = {} # Создан словарь.
    byte_number = [] # Создан список, элементами которого будут пары:
                     # (номер строки в файле, байт начала строки).
    for i in range(len(strings)):
        byte_number.append((i+1, nf.tell()))
        nf.write(strings[i] + '\n')
        string_positions[byte_number[i]] = strings[i]
    nf.close()
    return string_positions

sp1 = ['st1', 'st2', 'st3']

result = custom_write('pr.txt', sp1)
for elem in result.items():
    print(elem)
