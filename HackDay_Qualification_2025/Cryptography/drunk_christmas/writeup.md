# Drunk Christmas

## Clue / Information

Last year people were angry at my chall for needing the use of open-source tools such as bkcrack. This year's chall still has zips, but they have NO passwords. HA ! You still need to decrypt the flag, tho. glhf

challenges.hackday.fr:53073

## Resolution

Went to the url, where we simply have a prompt to upload a file.

I tried it with a Python script I made for another challenge.
It gave me back a `.zip` containing [a .md file](./READMEzip.md), my uploaded file with `.enc` added as file extension and _flag.txt.enc_.

**The following was a complete rabbit hole that had no link with the actual challenge, but well ¯\_(ツ)_/¯**

> Doing a `file` on the encrypted file I sent gives me: `Dyalog APL version 77.103`.
>
> Dyalog provides an environment for APL-based development.
>
> https://www.dyalog.com/
> https://hub.docker.com/r/dyalog/dyalog
>
> APL has an interpreter: https://www.gnu.org/software/apl/
>
> I tried running the `Dyalod APL` file with the interpreter: `apl -f [filename].enc` once with the `.enc` and once after renaming to `.aplf`. It didn't work.
>
> I tried using the docker image but it is not compatible with the platform I use (it expects `linux/amd64`).
>
> My guess is that we have to pass to the server an APL program that reads the `flag.txt.enc` file and then ... ¯\_(ツ)_/¯
>
> I tried doing a bunch of APL (Dyalog and GNU) function that reads the **flag.txt.enc** file but to no avail. Check [.apl.history](.apl.history) to see my poor attempts.

### author => [@komorebi](https://github.com/Killian-Morin)

## Write-Up

No official write-up yet

[@nhy42 - Drunk Christmas Write-Up](https://github.com/nhy42/nhy-write-ups/tree/main/Hackday/2025/Drunk%20Christmas)

[@merlleu - Drunk Christmas Write-Up](https://github.com/merlleu/public-writeups/blob/main/hackday2025_qualifiers/drunk_christmas.ipynb)