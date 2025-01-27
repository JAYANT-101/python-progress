#String are immutable you can make a new copy of it
a="!!!! harry !!!!!"
print(a.upper())
print(a.lower())
print(a.rstrip("!"))#will only strip post phix not pre phix
print(a.replace("harry","Jayant"))#will replace all acorence
print(a.split(" "))
blog="me dOIng PYTHon"
print(blog.capitalize())
str1="welcome to here"
print(str1.center(50))
print(a.count("harry"))
print(str1.endswith("here"))#can also chak  it any where by using index value 4,10
print(str1.find("to"))#if nothing found it gives 1
# print(str1.index("ishh")) will give an exseption if match no found
print(str1.isalnum())#will give ture if the  string is made of a-z and 0-9
print(a.islower())
print(a.isprintable())#if non-printable things used gives false like\n
print(str1.isspace())
print(str1.istitle())#ives ture of first letter is capital
print(str1.startswith("welcome"))
print(blog.swapcase())#swapes between upper and lower case both way
print(str1.title())