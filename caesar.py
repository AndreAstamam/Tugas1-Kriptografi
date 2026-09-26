ct = "JREUZ BLEF JVBRCZGLE KVKRG DVERIZB LEKLB UZGVCRARIZ YRIZ ZEZ"

def caesar_decrypt(text, k):
    res = []
    for c in text:
        if c.isalpha():
            res.append(chr((ord(c) - 65 - k) % 26 + 65))
        else:
            res.append(c)
    return "".join(res)

for k in range(14, 21):
    print(k, caesar_decrypt(ct, k))
