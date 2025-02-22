# Too many emojis

## Clue / Information

I like using emojis in my text messages, but my friend may have taken it too far. 💀 Can you figure out what she’s trying to tell me? 🤔

[emojis.png](./emojis.png)

## Resolution

We know the flag format is `bronco{}`, on the image some special characters: `{_}` are not encoded in emojis, that less to deal with.
The emojis are iOS.
The 6 first emojis, that translate to `bronco` each have the first letter of their Unicode name the letter corresponding to `bronco`:
:broken_heart: -> b
:relieved: -> r
...

Exception for :red angry face: since there is already :relieved: that corresponds to **r**, it corresponds to the second letter of the name: **e**

flag: `bronco{emojis_eXpress_my_emotions}`
