with open('test.txt','r') as f:
    print(type(f))
    #will read from 10 position byte
    f.seek(10)
    #will tell the above
    print(f.tell())
    # read the next 5 bytes
    data =f.read(5)
    print(data)
with open('test2.txt','w') as f:
    f.write("Jayant sinha")
    #will limit the input of the 5 bytes
    f.truncate(5)
with open('test2.txt','r') as f:
    print(f.read())