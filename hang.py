import random

print("You have six chances... Try to guess the word!! You don't lose a chance if your word is right!!\n\n")
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
           break
         
    else:
        counter = counter + 1
    gggg = " ".join(alt)
    ggg = "".join(alt)
    print(gggg)

    if ggg == word:
        break

    elif counter == 6:
        print("\n\nYou lose!!!")
        break
        

            

        

        
        
        
