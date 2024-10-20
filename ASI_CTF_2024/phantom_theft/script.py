import hashlib
import itertools

B58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

def base58_decode(s):
    x = 0
    for c in s:
        x = x * 58 + B58.index(c)
    return x.to_bytes(25, 'big')

def checksum(data):
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()[:4]

def is_valid_base58_address(address):
    try:
        decoded = base58_decode(address)
        if decoded[-4:] == checksum(decoded[:-4]):
            return True
    except ValueError:
        return False
    return False

# Example: Obfuscated address with `?` placeholders
obfuscated_address = "1????M?waN??9?P?o???sp???t?p??????"

# Find all positions of '?' in the address
missing_positions = [i for i, char in enumerate(obfuscated_address) if char == '?']

print("number of missing positions: ", len(missing_positions))

# Generate all combinations of missing characters
for replacement in itertools.product(B58, repeat=len(missing_positions)):
    candidate = list(obfuscated_address)
    for i, char in zip(missing_positions, replacement):
        candidate[i] = char
    candidate_address = ''.join(candidate)

    print(f"Testing address: {candidate_address}")

    # Check if the candidate address is valid
    if is_valid_base58_address(candidate_address):
        print(f"Valid Bitcoin address found: {candidate_address}")
        break
