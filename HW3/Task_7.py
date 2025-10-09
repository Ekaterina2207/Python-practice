word = input()
word_modify = ''.join(c for c in word if c.isalpha()).lower()
if word_modify == word_modify[::-1]:
    print(True)
else:
    print(False)