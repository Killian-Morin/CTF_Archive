from Crypto.Util.number import *

# Read the stored values from out.txt
with open('out.txt', 'r') as f:
    data = f.read().splitlines()
    n = int(data[0].split('=')[1])
    h = int(data[1].split('=')[1])
    hpq = int(data[2].split('=')[1])
    c = int(data[3].split('=')[1])

# Recover dinv from h (shift h back by z bits)
z = 567
dinv = h << z

# Recover d from dinv (inverse of dinv mod n)
d = pow(dinv, -1, n)

# Decrypt the ciphertext using the private key d
decrypted_message = pow(c, d, n)

# Convert the decrypted message from a long integer back to bytes
flag = long_to_bytes(decrypted_message)

# Print the recovered flag (message)
print(flag.decode())
