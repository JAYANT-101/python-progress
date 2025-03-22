import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
l=[]
k=int(input("Enter the number of name you want\n"))
for i in range(k):
    a=input("Enter name\n")
    l.append(a)
j=0
for i in l:
    speaker.Speak(f"{l[j]} is a mather choood")
    j=j+1