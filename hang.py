import random

words = ["hello", "bye", "dog", "python", "life", "happy"]

hmm = random.randint(0,len(words)-1)

for n in words[hmm]:
    print("_ ", end = "")

word = words[hmm]
alt = ["_ "] * len(word)
counter = 0

gg = 0
while gg == 0:
    take = input("\nWrite a single letter: ")

    for n in range(0,len(word)):
        if take == word[n]:
           alt[n] = word[n]
           counter = counter + 1

    print(alt)

    if counter == len(word):
        break
    

        

    

    
    
    
