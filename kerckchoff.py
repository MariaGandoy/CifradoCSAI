text = "IOLBSRODUWCCVQDNAKZGXSDWAHOLXWJTVBJTQLILGEUIFHLRDAALVKZXNFQKTDVEMWAEIVXRVDJPICMKKIIWDDGLMKXGEWJTNKIIJECUGBEEBHGETQKAEMQJJSUCUDVZLWHTJWMSAZVVTVVVMIRRVKBIJAAQLVIDWODUWBAZADTUIAUDLCMYJEJMHXDVUADLFOAHTVAGCTLVWKIJQGCAJAWOPIMUXSVLWAAWIUDNUWFIICAWHTGZGEAXMSEAIBAGDVKWUOPMJXNZBAPLRTAGERCKHITWJDNRDAGUJKGCFZVWBEEBLTLVBJPVRQDSEGTSREDMFISLVWHECMUIIFVVTVFAIJEJBADNJMLCOJZWEOEAWHLVLWREDJJTSVTGCLRDWGSZWFDFWQUXECTWFURBJTCRAVTPEMMBOEQWPTPXAFUVAGCTZLWCTZNATSGIJBICMKRLZMFISVBDTSVUHAOPMKSUEUSGCYMSJXRVABALFKPUMIYTSGMCXNVALPLVZLTLVTATUGZWHUDMVTCVAUDNKIEXNRBADNJMKIFVZETEKCFTNFBWSIENGGMRBADNVALTNMWQTERTGGGRVAHAKQGCMFVVXACMVTLRASCTVWEHMRQKIAELAHQLMDTSVFHTRKAUWIEWAHSVTSCCVVLHUITSEIJBWSUMQJJSGTMHIVCJHMVLWRIEADDCRCPHOEBJPPGMDTSRTGGDIMHDUIINDIIMPERZUWAELZACQLQWIUUMKJRCMIJIMIDTNKLMCESWMRLVEZPTJIHEPRAIJEJBADNUMKTMVZDPPRVAFUVQFHIJBWCTCMKPUKWJXTVADDCRTWHQLQJTFLBWCTCMPXSKMFREUMUDNKIEXNRBADNJQFIEIPMBAZVWH"

A = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06996,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.00150,0.01974,0.00074]

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def ceasar(text):
    Ai = [[0 for x in range(1)] for y in range(int((26)))]
    W = []
    prod = []

    for i in range(0,26):
        Ai[i] = A[i::]+A[:i:] #circular shifts are added to 2D array
        W.append(text.count(alpha[i])/float(len(text))) #Vector W is created as specified

    
    for i in range(0,26):
        summation = 0
        for j in range(0,25):
            summation += W[j]*Ai[i][j]
        prod.append(summation)

    location = prod.index(max(prod))

    key = alpha[location::]+alpha[:location:]

    return location


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

#split = [text[i:i+len(text)] for i in range(0, len(text), len(text))]

parts = [['' for x in range(1)] for y in range(int((length)))]

limit = len(text) - len(text)%length

for i in range(0,limit,length):
    for j in range(0,length):
        parts[j].append(text[i + j])

for i in range(limit,len(text)):
    parts[i-limit].append(text[i])

strings = [['' for x in range(1)] for y in range(int((length)))]

for i in range(0,length):
    strings[i] = ''.join(parts[i])

key = []

for i in range(0,length):
    key.append(ceasar(strings[i]))

result = []


for i in range(0,limit,length):
    for j in range(0,length):
        result.append(alpha[alpha.index(text[i+j])+key[j]-26])    
for i in range(limit,len(text)):
    result.append(alpha[alpha.index(text[i])+key[i-limit]-26])

final = ''.join(result)

print(key)
stri = ""
for i in key:
    stri += alpha[i]

print(stri)