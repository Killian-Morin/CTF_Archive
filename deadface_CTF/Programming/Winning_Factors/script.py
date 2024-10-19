from pwn import *

# Set architecture, os, and log level
context.arch = "amd64"
context.os = "linux"
context.log_level = "debug"

hostname = '147.182.245.126'
port = 33001

# Create a remote connection
p = remote(hostname, port)

# Read / ignore until the data that we want
p.recvuntil("Calculate the factorial of")
# Read the number, strip() to get rid of the spaces, pass from bytes to string and get rid of the trailing '.'
number = p.recvline().strip().decode()[:-1]
print(f"number: {number}") # Decode the bytes to string

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

factorial = factorial(int(number))
print(f"factorial: {factorial}")

# Send the factorial back to the server
p.send(f"{factorial}")
p.send(b"\n")

def print_lines(io):
    info("Printing io received lines")
    while True:
        try:
            line = io.recvline()
            success(line.decode())
        except EOFError:
            break

print_lines(p)

# When you're done, close the connection
p.close()
