from collections import Counter
text = open("text.txt",'r',encoding='utf8').read().lower()
box = text.split()

words3 = []
words5 = []
words7 = []
words10 = []
for x in box:
    if len(x) == 3:
        words3.append(x)
    if len(x) == 5:
        words5.append(x)
    if len(x) == 7:
        words7.append(x)
    if len(x) == 10:
        words10.append(x)

cntWords3 = Counter(words3)
cntWords5 = Counter(words5)
cntWords7 = Counter(words7)
cntWords10 = Counter(words10)

print(f"самое часто употребляемое слово из 3, 5, 7, 10 букв: {cntWords3.most_common(1)[0]}{cntWords5.most_common(1)[0]}{cntWords7.most_common(1)[0]}{cntWords10.most_common(1)[0]}")
print(f"самое редко употребляемое слово из 3, 5, 7, 10 букв: {cntWords3.most_common()[-1]}{cntWords5.most_common()[-1]}{cntWords7.most_common()[-1]}{cntWords10.most_common()[-1]}")