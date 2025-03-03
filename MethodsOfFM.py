'''
f=open('test.py','r')
i=0
while True:
    i=i+1
    line=f.readline()
    if not line:
        break
    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]
    print(f"Mark of the student {i} in english {m1}")
    print(f"Mark of the student {i} maths {m3}")
    print(f"Mark of the student {i} sst {m2}")
    '''
f=open('test.txt',"w")
line=['bababue\nnemu\n','hulahula']
f.writelines(line)
f.close()