### **7. Find the largest word in a sentence**

input = "hey my name is utkarsh"

split_input = input.split()

temp = ""

for i in split_input:
    if len(i) > len(temp):
        
        temp = i
        
print(temp)
