from random import randint
import string 
import numpy as np 
    
# Storing the value in variable result  
low=string.ascii_lowercase 
up = string.ascii_uppercase 
symba=["!","@","#","$","%","^","&","*","(",")","-"," ","_","+","=",",",".","/","\ ","]","[","?"]


def cypher(word):
  x=randint(1,100000)
  a=str(x)
  wor=list(word)
  cyk=""
  for i in range (len(wor)):
    if wor[i] in low:
      b=wor[i]
      b=low.index(b)
      b=b+x
      while b > 25:
        b=b-25
      k=low[b]
      cyk+=k
    elif wor[i] in up:
      b=wor[i]
      b=up.index(b)
      b=b+x
      while b > 25:
        b=b-25
      k=up[b]
      cyk+=k
    elif wor[i] in symba:
      k=wor[i]
      k=symba.index(k)
      k=k+x
      while k > 20 :
        k= k - 20
      b=symba[k]
      cyk+=b 
    else:
      k=str(wor[i])
      cyk+=k
  gyk=np.array([])
  gyk=np.append(gyk,a)
  gyk=np.append(gyk,cyk)
  return (gyk)


def decyp (word):
  wor=list(word)
  res=int(wor[0])
  kaz=str(wor[1])
  kaz=list(kaz)
  work=""
  for i in range (len(kaz)):
    if kaz[i] in low:
      k=kaz[i]
      b=low.index(k)
      b=b-res
      while b < 0 :
        b=b+25
      k=low[b]
      work+=k
    elif kaz[i] in up:
      k=kaz[i]
      b=up.index(k)
      b=b-res
      while b < 0:
        b=b+25
      k=up[b]
      work+=k    
    
    elif kaz[i] in symba:
      k=kaz[i]
      b=symba.index(k)
      b=b-res
      while b < 0:
        b=b+20
      k=symba[b]
      work+=k  
    else:
      work+=kaz[i]
  print (work)

x=str(input("Input word\n"))
gav=cypher(x)
print (gav)
decyp(gav)

  

    

