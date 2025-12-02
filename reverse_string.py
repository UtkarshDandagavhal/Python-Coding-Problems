# Reverse the string

input = "utkarsh"

n = len(input)

temp = ""

#   WAY 1
# for i in range(n-1,-1,-1):
#     temp += input[i]
    
    
# print(temp)

# WAY 2
# for i in input[::-1]:
#     temp+=i

# print(temp)

# WAY 3
print(input[::-1])
    
