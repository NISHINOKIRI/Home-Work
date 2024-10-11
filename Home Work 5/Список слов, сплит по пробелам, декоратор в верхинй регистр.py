def get_split_words_list():
    words_list = input('Enter some words (separated by spaces) :\n').split()
    return words_list

''' Здесь переменная words_list 
это список, который был получен от функции get_split_words_list()
таким образом, когда shown_word_list вызывается, words_list будет содержать этот список слов '''
def shown_word_list(words_list):
    print('\nWords list:')
    print(words_list)

def dec_up_reg(func):
    def zalupper(words):
        result = func(words)
        return [word.upper() for word in result]
    return zalupper

@dec_up_reg
def show_words(words):
    return words

def print_result():
    words = get_split_words_list()
    shown_word_list(words)
    upper_words = show_words(words)
    print('\nUppercase word:\n' + ', '.join(f'"{word}"' for word in upper_words) + ';')

print_result()
