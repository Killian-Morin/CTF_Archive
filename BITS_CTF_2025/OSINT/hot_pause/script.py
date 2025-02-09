from pwn import *
from print_color import print

# Set architecture, os and log level
context(arch="amd64", log_level="debug")

p = remote('chals.bitskrieg.in', 8000)

cityname = "Ahmedabad"

block = "Q3"

p.sendlineafter("City Name (all caps): ", cityname.upper())
data = p.recvline()
if data != b"Wrong answer. Exiting...\n":
    print(f"CORRECT: {cityname}", color='blue')


# script used for the second question
# blockletter = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R"]

# for letter in blockletter:
#     for nb in range(1, 10):
#         p = remote('chals.bitskrieg.in', 8000)
#         p.sendlineafter("City Name (all caps): ", cityname.upper())

#         # attempt = letter + nb
#         attempt = letter + str(nb)
#         p.sendlineafter("Block Letter with Bay(For eg. A5,B1 etc.): ", attempt)
#         data = p.recvline()
#         if data != b"Wrong answer. Exiting...\n":
#             print(f"CORRECT: {attempt}", color='blue')
#             exit()
#         else:
#             print(f"{attempt}", color='red')

#         p.close()

# p.close()

p.sendlineafter("Block Letter with Bay(For eg. A5,B1 etc.): ", block)
data = p.recvline()
if data != b"Wrong answer. Exiting...\n":
    print(f"CORRECT: {block}", color='blue')

# script for the third question
color = [
    "700 700 700 700 1400 1400 1400 2800 700 2100 700 700 700 1400 700 1400 700 700 700 2100 1400 2800 700",
    "700 700 700 700 1400 1400 1400 2800 700 1400 700 700 1400 1400 700 700 700 700 700 2800 1400 2800 700",
    "1400 1400 700 700 700 1400 700 2800 700 1400 700 700 700 700 700 700 700 1400 1400 2800 1400 2800 700",
    "1400 1400 700 700 700 700 1400 2800 700 2100 700 700 700 1400 700 1400 1400 2800 1400 2800 700",
    "1400 1400 700 700 700 700 700 700 700 2100 700 2100 700 700 700 1400 700 1400 1400 2800 1400 2800 700",
    "700 700 700 700 1400 1400 1400 2800 700 2100 1400 2100 700 2100 1400 2100 1400 2800 700",
    "700 700 700 2100 1400 1400 700 2100 700 1400 700 700 700 2800 1400 1400 700 2100 1400 2800 700",
    "700 700 700 2100 1400 1400 700 2100 700 1400 700 700 700 1400 700 700 1400 1400 700 700 1400 700 700 2800 700",
    "700 700 700 2100 1400 700 700 2800 700 1400 700 700 700 1400 700 700 1400 1400 700 700 1400 700 700 2800 700",
    "1400 1400 700 700 700 2100 700 2100 700 2100 1400 700 700 700 700 2100 700 2800 1400 2800 700",
    "1400 1400 700 700 700 2100 700 2100 700 1400 700 700 700 700 700 700 700 1400 1400 2800 1400 2800 700",
    "1400 1400 700 700 700 1400 700 2800 700 2100 1400 700 700 700 700 2100 700 2800 1400 2800 700"
    ]

for c in color:
    p = remote('chals.bitskrieg.in', 8000)
    p.sendlineafter("City Name (all caps): ", cityname.upper())

    p.sendlineafter("Block Letter with Bay(For eg. A5,B1 etc.): ", block)

    p.sendlineafter("Data Stream: ", c)
    data = p.recvline()
    if data != b"Wrong answer. Exiting...\n":
        print(f"CORRECT: {c}", color='blue')
        exit()
    else:
        print(f"{c}", color='red')

    p.close()
