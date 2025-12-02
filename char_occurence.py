# *4. Count occurrences of each character**


input = "banana"
temp_dict = {}

# WAY 1
# for i in input:
#     if i in temp_dict:
#         temp_dict[i]+=1
#     else:
#         temp_dict[i] = 1
        
# print(temp_dict)

# WAY 2
for i in input:
    temp_dict[i] = temp_dict.get(i,0)+1
    
print(temp_dict)
    
