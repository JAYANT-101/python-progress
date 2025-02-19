dic ={
    "jayant": "human","sinha":"is a last name"
}
print(dic["jayant"])#will throw a error when key is not found
print(dic.get("sinha"))#will not throw a error
print(dic.keys())#will only print keys
print(dic.values())
# for i in dic.keys():
#     print(f"the key are for {i} is {dic[i]}")
print(dic.items())
for key,value in dic.items():
    print(f"the ker are {key} and values are {value}")