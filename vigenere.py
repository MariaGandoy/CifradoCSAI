#https://github.com/Taloohi/Vigenere-Cipher                             -- Obtención de la longitud de la llave

#https://github.com/savanddarji/Cracking-a-Vigenere-Cipher/tree/master  -- Obtención de la llave y base general


from __future__ import division
from math import gcd
import string
import numpy as np
import argparse


def shift(l1,n1): # for left shift operation
    return l1[n1:] + l1[:n1]
num = dict(zip(range(0,26),string.ascii_lowercase))# for reverse mapping: numbers to letter
A = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,
     0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.0236,0.0015,0.01974,0.00074]

a9=['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
    'o','p','q','r','s','t','u','v','w','x','y','z']


##Pillar archivo desde línea de comandos

parser = argparse.ArgumentParser(description="Lee un texto cifrado desde un archivo")
parser.add_argument(
    "archivo",
    type=str,
    help="Nombre del archivo con el texto cifrado"
)

args = parser.parse_args()


try:
    with open(args.archivo, 'r') as archivo:
        a = archivo.read().lower()
except FileNotFoundError:
    print("Archivo no encontrado.")

a=list(a)

#####################    GET LENGTH KEY     ##########################
##### Inicia código de #https://github.com/Taloohi/Vigenere-Cipher 
text=a

displacement = []

for i in range(0,21):
    displacement.append(text[i::]+text[:i:])

N = [0]

for i in range(1,len(displacement)):
    sum = 0
    for j in range(0,len(text)):
        if displacement[i][j] == text[j]:
            sum += 1
    N.append(sum)

largest = max(N)

first = max(N)
second = 0

for i in range(0,len(N)):
    if N[i] > second and N[i] != max(N):
        second = N[i]
        
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

length = gcd(N.index(first),N.index(second))

##### Fin código de #https://github.com/Taloohi/Vigenere-Cipher 

L=length
#####################    dividing in L(max d) parts     ##########################
z=[[]for x1 in range(0,L)]
v1=0
while v1<L:
    for i2 in range(v1,len(a),L):
        z[v1].append(a[i2])
    v1+=1
######################     cracking caesar cipher    ##############################
v1=0
Array=[]
while v1<L:
    W=[]
    for charc in a9:
        b1 = z[v1].count(charc)
        b1 = b1/26
        b1 = round(b1,7)
        W.append(b1)
    I =24
    J=[]
    t=0
    while I>=0:
        B= shift(A,t)
        K = np.dot(W,B)
        K = round(K,6)
        J.append(K)
        I -= 1
        t+=1
    Max1=max(J)#for highest number in the list
    F = [D for D, E in enumerate(J) if E==Max1]# retrieve the index of the maximum number
    F[0]=((26-F[0])%26)
    key=num[F[0]].upper()
    Array.append(key)
    S1=[]
    for character in z[v1]:#loop for getting deciphered numbers
        number = ord(character) - 97
        number = ((number - F[0])%26)
        S1.append(number)
    a2=[]
    for id2 in S1:# loop for number to alphabet mapping
        a2.append(num[id2])
    z[v1]=a2
    v1+=1



print ('LLAVE:',''.join(Array))