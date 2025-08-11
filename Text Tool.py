
text=input("enter your text: ").split()
txt=[]
repeat=[]
for i in text:
    if i not in txt:
        txt.append(i)
    else:
        repeat.append(i)    
print(f"Repeated words are: {repeat}") 
l=len(txt)
s=0
for i in txt:
    s+=len(i)
print(f"motevaset tol kalamat: {s/l}")
print(min(txt))
print(max(txt))
a=[]
for i in txt:
    if i[0]=='a':
        a.append(i)
print(f"start with a={a}")
b=[] 
for i in txt:
    if i[0]==i[-1]:
        b.append(i)
print(f"start and end is equal={b}") 
txt.sort()
for i in txt:
    print("* "* len(i))
     



        





               

