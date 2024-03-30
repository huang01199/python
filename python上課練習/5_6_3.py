word="elephant"
word_count={letter: word.count(letter)for letter in set(word)}
for i in word_count:
    print(i,word_count[i])