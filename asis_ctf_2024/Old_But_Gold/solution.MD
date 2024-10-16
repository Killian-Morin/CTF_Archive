```
openssl aes-256-cbc -a -salt -pbkdf2 -kfile key.txt -in flag.txt -out flag.enc
```

`aes-256-cbc` -> type of encryption algo to use
AES (Advanced Encryption Standard) with a 256-bit key size in CBC (Cipher Block Chaining) mode

`-a` -> base64 process the data. at encryption it means the data will be base64 encoded. at decryption the input data is base64 decoded before being decrypted.

`-salt` -> use a random salt when deriving the encryption key. this adds randomness to the key derivation process

`-pbkdf2` -> use pbkdf2 (Password-Based Key Derivation Function 2) to derive the encryption key from the password. this function applies a hash function multiple times to a password.

`-kfile key.txt` -> read the first line of key.txt that will be used as password, it's use to derive the actual the actual key which is used to encrypt the data

`-in flag.txt` -> input file, i.e. the flag

`-out flag.enc` -> output file, i.e. the flag after encryption

https://superuser.com/questions/1329658/how-can-i-encrypt-decrypt-aes-256-cbc-with-openssl
https://stackoverflow.com/questions/16056135/how-to-use-openssl-to-encrypt-decrypt-files


from what I understand, the goal is to get back `flag.txt`. We have the command that was used to produce `flag.enc` and `key.corrupted`.
`flag.enc` is the result of the encryption of the `flag.txt`.
`key.corrupted` is a corrupted version of the key that was used during the process of encryption of the file.


`hexdump -C key.corrupted` -> 4 premiers bits: 58 41 52 3f = XAR?
https://en.wikipedia.org/wiki/Xar_%28archiver%29
- archive xar has his 4 first bytes as `XAR!`
- the bytes 24 to 28 are the checksum algorithm, here it's `00 00 00 03` so it checks out that the checksum algorithm is = 3 = SHA-256


Normally flag.enc is base64 encoded, so if I try to decode it:
- `U2FsdGVkX18pCSq6f3rc6oVWVxDmkUL5inWefNmn3ljGBXkGNBs86jE2u1MfrqlS` = `Salted__)￹*�￹z��￹VW￹�￹B�￹u￹|٧�X�￹y￹4￹<�16�S￹��R`

- `rrTh4ZPBQy8Eb3BUMfPHXTbdUR0nVlnc5devkaHDigfhPHo+w1TMozVjzMDfX39+` = `����￹�C/￹opT1��]6�Q￹'VY��ׯ￹��￹�<z>�Ṭ5c���_￹~`
hexdump this gives nothing interesting