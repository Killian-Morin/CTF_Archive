# subject
The Alchemist challenge involves an encryptor for any file, and your task is to reverse engineer it to successfully decrypt the content.

# process

- opened `alchemist` in IDA64 and BinaryNinja
- go to main function and pseudo code
- it prints `ASIS` to stdout (consistent from what we see in flag.enc)
  since it's an encryptor that gives an archive I suppose that ASIS is considered the file signature
- memset a variable of type `void` with a size of 255
- it prints some things to stdout (0x909d1f, 0x909d, 0x90)
- get an input taken from stdin and saves it as an int
  potentially the fd of the file you want to encrypt, since it does not use open() anytime
- this int must be >= 0 for the program to execute some meaningful things
- sets some variables and start a `while(true)` loop
  in this loop, reasks for an input on stdin, the character to encode, the size of the file


- at the end it prints `BYE!` to stdout (consistent from what we see in flag.enc)