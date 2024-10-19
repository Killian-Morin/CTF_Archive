# Clue / Information
We captured a DEADFACE laptop! During our forensics, we discovered a file with a weird tag that said “Hidden Treasure Here”. Can you find the treasure's identification code using the image file?

Submit the flag as flag{flagtext}. The flag will begin with a G.

SHA1: 4c3cad926969e1e5a214f15fa67d7d330e13c33b

# Resolution

With the 'flag will begin with a G' I tried to see if there was relevant data using `strings OSINT07.png | grep '^G'`.
The first line of the ouput is `Greenshot^U`. [Greenshot](https://getgreenshot.org/)
