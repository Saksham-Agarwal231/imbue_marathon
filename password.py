import random

hello = "qwertyuioplkjhgfdsazxcvbnm12345678890QWERTYUIOPLKJHGFDSAZXCVBNM!@#$%^&*()"
yo = ""

for n in range(12):
    hehe = random.randint(0,len(hello)-1)
    yo = yo + hello[hehe]
  

print(yo)

    
    
    
