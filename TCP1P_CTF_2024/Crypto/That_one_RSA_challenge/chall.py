from Crypto.Util.number import *
from secret import flag

# z is a shifting parameter (its purpose will be seen later when calculating h and hpq)
z = 567

# Generate two large 1024-bit prime numbers p and q
p = getPrime(1024)
q = getPrime(1024)

# Calculate modulus n (product of p and q) which is used for RSA encryption
n = p*q

# Convert the flag (the message) from bytes to a long integer and encrypt it using the RSA public exponent 65537
c = pow(bytes_to_long(flag), 65537, n)

# Calculate Euler's Totient function, which is used for generating the private key
tot = (p-1) * (q-1)

# Calculate the private exponent d (the multiplicative inverse of 65537 mod tot)
d = int(pow(65537, -1, tot))

# Calculate dinv, the inverse of d modulo n
dinv = int(pow(d, -1, n))

# Shift dinv to the right by z bits and store it in h
h = int(dinv >> z)

# Shift the sum of p and q to the right by z bits and store it in hpq
hpq = (int((p+q)>> z))

with open('out.txt', 'w+') as f:
    f.write(f'{n=}\n')
    f.write(f'{h=}\n')
    f.write(f'{hpq=}\n')
    f.write(f'{c=}\n')
