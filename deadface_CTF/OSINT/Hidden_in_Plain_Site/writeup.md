# Clue / Information
We captured a DEADFACE laptop! During our forensics, we discovered a file with a weird tag that said “Hidden Treasure Here”. Can you find the treasure's identification code using the image file?

Submit the flag as flag{flagtext}. The flag will begin with a G.

SHA1: 4c3cad926969e1e5a214f15fa67d7d330e13c33b

# Resolution

With the 'flag will begin with a G' I tried to see if there was relevant data using `strings OSINT07.png | grep '^G'`.
The first line of the ouput is `Greenshot^U`. [Greenshot](https://getgreenshot.org/)

https://www.google.com/maps/@38.9701532,-104.7503935,3a,75y,312.17h,85.7t/data=!3m6!1e1!3m4!1sZrxZr4iGQnD_7Wsqe5F8-g!2e0!7i16384!8i8192?hl=en&coh=205409&entry=ttu&g_ep=EgoyMDI0MTAxNi4wIKXMDSoASAFQAw%3D%3D -> thanks discord !!

So the thing that is obfuscated is the name of the road: `Royal Pine Dr`.
