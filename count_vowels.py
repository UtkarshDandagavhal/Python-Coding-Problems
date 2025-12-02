### **3. Count vowels in a string**

input = "hello world"

count = 0

# vowels = "aeiou"
# for i in input:
#     if i in vowels:
#         count+=1

# print(count)

temp = ""
vowels = {"a","e","i","o","u"}
for i in input.lower():
    if i in vowels:
        temp+=i
        count+=1
        
print(count)
print(temp)
