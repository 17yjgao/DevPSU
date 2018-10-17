consonant = "bcdfghjklmnpqrstvwxz"
vowel = "aeiou"
#x = input("input a phrase")
x = "i cant speak pig latin"
sentence = x.split(" ")
finished = []
counter = 0
for n in sentence:
    if n[0] in consonant:
        while n[counter] in consonant:
            counter +=1
        finished.append(n[counter:] + n[0:counter] + "ay")
    else:
        finished.append(n+"yay")
    counter = 0
finished_sentence =   " ".join(finished)
#print(finished)
print (finished_sentence)
