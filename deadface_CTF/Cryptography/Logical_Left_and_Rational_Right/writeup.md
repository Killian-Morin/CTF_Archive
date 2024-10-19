# Clue / Information
DEADFACE left this artifact with one of their victims. Can you decipher what it says?

Submit the flag as flag{flag-text}

SHA1: 60405cade14b21f385265c4e5e0efadbc971e607

# Resolution
Content of the file:
```
\/\\/\/\ \///\/\/ \///\\// \///\/\\ \\/\\\\\ \//\\\\/ \\/\\\\\ \//\//\\ \//\/\\/ \///\/\\ \///\/\\ \//\//\\ \//\\/\/ \\/\\\\\ \///\\// \//\//// \//\//\/ \//\\/\/ \///\/\\ \//\/\\\ \//\/\\/ \//\///\ \//\\/// \\/\\\\\ \///\/\\ \//\//// \\/\\\\\ \//\\/// \//\\/\/ \///\/\\ \\/\\\\\ \///\\// \///\/\\ \//\\\\/ \///\\/\ \///\/\\ \//\\/\/ \//\\/\\ \\/\//\\ \\/\\\\\ \//\/\\\ \//\//// \///\\\\ \//\\/\/ \\/\\\\\ \////\\/ \//\//// \///\/\/ \\/\\\\\ \//\/\\\ \//\\\\/ \///\//\ \//\\/\/ \\/\\\\\ \//\\//\ \///\/\/ \//\///\ \\/\\\\\ \///\/\\ \//\/\\\ \//\/\\/ \///\\// \\/\\\\\ \////\\/ \//\\/\/ \//\\\\/ \///\\/\ \\/\\\\\ \/\/\/\\ \///\/\/ \///\\/\ \//\\\/\ \//\//// \\/\\\\\ \/\/\/\\ \//\\\\/ \//\\\// \//\/\// \////\\/ \\/\\\\/ \\/\\\\/ \\/\\\\/ \\/\\\\/ \\/\\\\\ \//\\//\ \//\//\\ \//\\\\/ \//\\/// \////\// \/\\/\\\ \\//\\// \/\//\\/ \/\//\\/ \\//\\\\ \/\/\/\/ \///\\/\ \/\\\//\ \\//\\\/ \/\\///\ \\//\/\\ \\//\\\/ \\//\\\/ \/\//\\/ \\//\/\\ \/\/\/// \\//\/\\ \/\\/\// \\//\\// \/////\/
```

This could be a form of visual encoding or representation of binary data.

The name of the challenge suggests that the encoding may involve interpreting slashes (/, \) in a left-right or binary manner, likely representing 0 and 1.

Just have to write a script that maps the slashes to 0 and 1 and convert the obtained binary to ASCII.

We end up with the following text: `Just a little something to get started, hope you have fun this year Turbo Tacky!!!! flag{H3YY0UrF1N411Y4W4K3}`

The flag is: `flag{H3YY0UrF1N411Y4W4K3}`
