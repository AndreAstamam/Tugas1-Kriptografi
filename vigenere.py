from collections import Counter

ct_raw = "CYGKIZ EBNWW XNNIW GNVZSEF XQQYAGZO XNRID XVCVKFVUQC MRRMBNV UIXXV EIOMNT BOLCKAKB"
ct = ct_raw.replace(" ", "")

indo_freq = {
    'A': 16.0, 'N': 8.5, 'E': 8.2, 'I': 7.6, 'K': 5.4, 'T': 5.0, 'R': 5.0,
    'U': 4.8, 'D': 4.5, 'S': 4.5, 'M': 3.5, 'B': 3.2, 'G': 3.0, 'P': 3.0,
    'L': 3.0, 'H': 2.5, 'Y': 2.0, 'C': 1.8, 'J': 1.2, 'W': 1.2, 'O': 1.5,
    'F': 0.3, 'V': 0.2, 'Z': 0.1, 'X': 0.05, 'Q': 0.1
}

def vig_decrypt(text, key):
    res = []
    for i, c in enumerate(text):
        k = ord(key[i % len(key)]) - 65
        res.append(chr((ord(c) - 65 - k) % 26 + 65))
    return "".join(res)

def text_chi2(text):
    counts = Counter(text)
    n = len(text)
    chi2 = 0
    for letter, exp_pct in indo_freq.items():
        expected = n * exp_pct / 100
        observed = counts.get(letter, 0)
        chi2 += (observed - expected) ** 2 / (expected if expected > 0 else 1)
    return chi2

candidate_keys = ["KUNCI", "SANDI", "RAHIA", "ANGKA", "HURUF", "ANDRE", "KODEK", "GESER", "PUTAR", "ACAKI"]

best_key, best_score = None, None
for key in candidate_keys:
    pt = vig_decrypt(ct, key)
    score = text_chi2(pt)
    if best_score is None or score < best_score:
        best_score, best_key = score, key

print("KEY:", best_key)
print("PLAINTEXT:", vig_decrypt(ct, best_key))
