from fita import Word

word="000111"

obj_word = Word(word)
def a(word):
    word.word = word.word[2:]

a(obj_word)
print(obj_word.word)
        
