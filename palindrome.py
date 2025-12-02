### **2. Check if a string is a palindrome**

input = "Eve"

convert_lower = input.lower()

temp = ""

for i in convert_lower[::-1]:
    temp += i
    
print(temp)

if temp == convert_lower:
    print(True)
else:
    print(False)

