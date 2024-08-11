class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)


    def get_all_words(self):
        all_words = {}
        for i in range(len(self.file_names)):
            all_file_words = '' # Строка из всех слов одного файла.
            Sp_words = [] # Список из всех слов одного файла.
            with open(self.file_names[i], 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    for char in line:
                        if char == '?' or char == '!' or char == '.' or char == ',' or char == ';' or char == ':' or char == '-':
                            line = line.replace(char, '')
                    all_file_words = all_file_words + line # Формирование одной строки из всех
                                                            # строк файла (сложение строк файла).
                    Sp_words = all_file_words.split() # Преобразование строки из слов в список слов файла.
            all_words[self.file_names[i]] = Sp_words # Присвоение ключу file_names[i] знаения Sp_words.
        return all_words

    def find(self, word):
        word = word.lower()
        Res_find = {} # Создание словаря.
        for name, Sp_words in self.get_all_words().items():
            for i in range(len(Sp_words)):
                if Sp_words[i] == word:
                    Res_find[name] = i + 1 # Добавление пары [name, i + 1] ([ключ, значение]) в словарь.
                    break
        return Res_find

    def count(self, word):
        word = word.lower()
        Res_count = {} # Создание словаря.
        for name, Sp_words in self.get_all_words().items():
            j = 0 # Счётчик повторений слова word.
            for i in range(len(Sp_words)):
                if Sp_words[i] == word:
                    j += 1
                Res_count[name] = j # Добавление пары [name, j] ([ключ, значение]) в словарь.
        return Res_count


# Поиск в тестовом файле.
# T = WordsFinder(['test_file.txt'])
# print(T.get_all_words()) # Все слова
# print(T.find('TEXT')) # 3 слово по счёту
# print(T.count('teXT')) # 4 слова teXT в тексте всего

# Поиск во всех стихотворениях
finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))





