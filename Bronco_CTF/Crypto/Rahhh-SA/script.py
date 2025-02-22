#!/usr/bin/python3

# Given values
e = 65537
n = 3429719
p = -811
ciphertext = [-53102, -3390264, -2864697, -3111409, -2002688, -2864697, -1695722, -1957072, -1821648, -1268305, -3362005, -712024, -1957072, -1821648, -1268305, -732380, -2002688, -967579, -271768, -3390264, -712024, -1821648, -3069724, -732380, -892709, -271768, -732380, -2062187, -271768, -292609, -1599740, -732380, -1268305, -712024, -271768, -1957072, -1821648, -3418677, -732380, -2002688, -1821648, -3069724, -271768, -3390264, -1847282, -2267004, -3362005, -1764589, -293906, -1607693]

# Step 1: Compute q
q = n // p
print(f"q = {q}")

# Step 2: (p-1)*(q-1) i.e. Euler's totient function phi(n)
phi_n = (abs(p) - 1) * (abs(q) - 1)
print(f"phi(n) = {phi_n}")

# Step 3: Compute the private exponent d i.e. d ≡ e^(-1) mod phi(n)
d = pow(e, -1, phi_n)
print(f"d = {d}")

# Step 4: Decrypt the ciphertext: m = c^d % n
decrypted_message = []
for c in ciphertext:
    # unnecessary step here: convert negative ciphertext to positive equivalent modulo n
    # c_pos = c + n
    # Decrypt using modular exponentiation
    m = pow(c, d, n)
    decrypted_message.append(m)
print(f"Decrypted message (as numbers): {decrypted_message}")

# Convert the decrypted numbers to ASCII characters
decrypted_text = ''.join([chr(m) for m in decrypted_message])
print(f"Decrypted message (as text): {decrypted_text}")