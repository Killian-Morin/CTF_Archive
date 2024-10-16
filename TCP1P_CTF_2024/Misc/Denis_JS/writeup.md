# Clue / Information
none / not relevant

# resolution
(thanks chatgpt)
The JavaScript runs with Deno (open-source runtime).
Some of its functions allow to interact with what acts as backend.
From the Dockerfile we know that the file holding the flag begins with `/flag-` and the rest is a randomly and modified list of characters.

To connect to the server I used nc with the address and port provided by the challenge.
This gives me an input field to inject what I want.

I solved it in two steps:
- get the full name of the flag (/flag-XXXXX):
  - connect to the server, I used nc
  - send as input: `for (const entry of Deno.readDirSync("/")) {if (entry.name.search("flag-") != -1) console.log(entry)}`
  - Deno.readDirSync() returns an iterable object with the directory entries, each object has a 'name' attribute

- read the file with the name obtained:
  - connect to the server, I used nc
  - send as input: `Deno.readTextFileSync('/flag-XXX')`
  - to have error message: `try {Deno.readTextFileSync('/flag-XXXX');} catch (e) {e.name + ': ' + e.message}`
  - This will read the flag and output the flag !

# Fixup
There was a trivial bug on our previous calculator's code. Hopefully, this time there won't be a any issues :(