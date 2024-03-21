import re
from collections import Counter

def count_words(text):
    words = re.findall(r'\w+', text.lower())
    word_count = Counter(words)
    return word_count

def main():
    print('Word Counter')
    print('------------')

    while True:
        user_input = input('Enter text or "quit" to exit: ')
        if user_input == 'quit':
            print('Thanks for using Word Counter!')
            break

        word_count = count_words(user_input)
        print('\nWord count:')
        for word, count in word_count.items():
            print(f'{word}: {count}')

if __name__ == '__main__':
    main()
