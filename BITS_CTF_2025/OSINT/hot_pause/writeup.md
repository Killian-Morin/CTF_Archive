# Hot Pause

## Clue / Information

What even is OSINT about this?

[concert.mp4](./concert.mp4)

`nc chals.bitskrieg.in 8000`

## Resolution

When running `nc chals.bitskrieg.in 8000` we end up with the following:
```bash
> nc chals.bitskrieg.in 8000
Welcome secret agent. We've recovered a video from our aliases infiltrating our next target. Your first task is to find out what is our target city.
City Name (all caps):
```

The group name is **Coldplay**. The song name is **Yellow**.

City Name attempts:
"BUENOS AIRES", "LOS ANGELES", "BERLIN", "MALIBU", "LONDON", "NEW YORK CITY", "DUBAI", "INGLEWOOD", "MELBOURNE", "HINTON Charterhouse", "Rancho Santa Fe ", "Athens", "Paradise", "Vancouver"

Since this CTF is made by Indian, I tried to search for the latest Coldplay concert in India: https://www.concertarchives.org/bands/coldplay?date=past. The latest concert done at the time was in **Ahmedabad** in the **Narendra Modi Stadium**.

```bash
City Name (all caps): AHMEDABAD
Correct!
Well done! Now you need to find out where our partner agent was sitting.
Block Letter with Bay(For eg. A5,B1 etc.):
```

I found this seating row plan on the stadium: https://stadiumsguide.com/wp-content/uploads/2023/09/narendra-modi-stadium-seating-plan-rows-stands-982x1024.jpg

Since I did not want to try each Block letter and bay I made a script with the possible block letter and bay number.
The correct one was **Q3**.

```bash
Well done! Now you need to find out where our partner agent was sitting.
Block Letter with Bay(For eg. A5,B1 etc.): Q3
Correct!
Good work. Now when you hear Chris Martin say "You know I love you so...." for the beat drop, I need you to use your Flipper Zero to send the correct data stream, replicating the wristbands colour exactly. Our enemies should have no clue. Good Luck.
Data Stream:
```

Since the song name is 'Yellow' and from the video I will take the color yellow as the `wristbands colour` that we need to `replicate exactly`.

Another team member found the following repo: https://github.com/danielweidman/flipper-pixmob-ir-codes that has a list of colors to `Control your PixMob wristbands at home with a Flipper Zero!`

In the file [pixmob_all_colors.ir](https://github.com/danielweidman/flipper-pixmob-ir-codes/blob/main/pixmob_all_colors.ir) there is the smallest list of colors.

The same teammate also made a script with `pwntools` and downloaded the file to parse it, take the `data` value of each entry and try it.

For my part I took all colors with `YEL` in it and put them in an array of string to also try each value.

Finally the correct color data was `1400 1400 700 700 700 700 1400 2800 700 2100 700 700 700 1400 700 1400 1400 2800 1400 2800 700` that corresponds to the `YEL` entry.

Flag: `BITSCTF{that_was_a_very_weird_OSINT_challenge_afd12df}`
