# Who cares about SSI anyway ?

## Clue / Information

A system administrator, frustrated after a heated debate about cybersecurity standards, ended up creating a poorly secured cheat sheet. Convinced that he could outsmart his own cybersecurity experts, he disregarded some basic principles. The result? A vulnerable document that might hold sensitive information. Can you uncover his mistakes and decipher the secrets hidden ?

`challenges.hackday.fr:48118`

## Resolution

SSI -> Sécurité des Systèmes d'Information ~ Computer Security

After going to the specified address on a browser, querying it with `curl`, I tried to connect to it with `nc` and there I got the prompt:
`Can you find the flag?
Your try? `

So next step is doing a Python script and using `pwntools` to try some things.

At first did a loop that sends a string of changing size to see if at one point I have a different response than `Wrong length`

```python
for i in range(0, 100):
    payload = b"a" * i
    p.sendlineafter("Your try? ", payload)
    data = p.recvline()

    if data == b'Wrong length\n':
        print(f"WRONG LENGTH {i}", color='red')
    else:
        print(data, tag='success', color='green')
        break
```

With a payload of length **21** (not including the `\n`) I get as a response `Incorrect` some progress ! So it seems that the flag has a length of 21.

### author => [@komorebi](https://github.com/Killian-Morin)

## Write-Up

[Official Write-Up](https://github.com/ChallengeHackDay/qualif-2025/blob/main/PROG/Who%20cares%20about%20SSI%20anyway/solve/wu.md)

[@merlleu - Who cares about SSI anyway ? Write-Up](https://github.com/merlleu/public-writeups/blob/main/hackday2025_qualifiers/ssi.ipynb)
