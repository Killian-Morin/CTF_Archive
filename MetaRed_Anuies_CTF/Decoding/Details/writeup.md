# Clue / Information
not noted

# writeup
1. Extract ppt
2. Go to ppt/media
3. Find file.png
4. file reveals it is ASCII, turns out it is base64 encoded
5. `cat file.txt | base64 -d > new`
6. file new -> PNG, opening shows the flag.