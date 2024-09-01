class WordsFinder:
    def __init__(self, file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        words = ''
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        with open(self.file_names, encoding='utf-8') as file:
            for line in file:
                line = line.lower()
                for i in line:
                    if i in punctuation:
                        line = line.replace(i, '')
                words += line
            all_words.update({self.file_names: words.split()})

        return all_words

    def find(self, name):
        dict1 = {}
        for key, value in self.get_all_words().items():
            if name.lower() in value:
                dict1[key] = value.index(name.lower()) + 1
                return dict1

    def count(self, name):
        dict1 = {}
        for value, key in self.get_all_words().items():
            words = key.count(name.lower())
            dict1[value] = words
        return dict1


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
