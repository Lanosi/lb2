from collections import Counter

text = open("text1.txt", 'r', encoding='utf8').read().lower()
words = text.split()

box_word = {3: [], 5: [], 7: [], 10: []}

for word in words:
    if len(word) in box_word:
        box_word[len(word)].append(word)
print(box_word)

counters = {length: Counter(word_list) for length, word_list in box_word.items()}

max_many_words = {length: counter.most_common(1)[0] for length, counter in counters.items() if counter}
min_many_words = {length: counter.most_common()[-1] for length, counter in counters.items() if counter}

print(f"самое часто употребляемое слово из 3, 5, 7, 10 букв: {max_many_words[3]} {max_many_words[5]} {max_many_words[7]} {max_many_words[10]}")
print(f"самое редко употребляемое слово из 3, 5, 7, 10 букв: {min_many_words[3]} {min_many_words[5]} {min_many_words[7]} {min_many_words[10]}")
