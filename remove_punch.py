### **8. Remove punctuation from a string**
input = '`"hello!!!"`'

punctuations = '!`"'

no_punc = ""

for i in input:
    if i not in punctuations:
        no_punc += i
        
print(no_punc)

