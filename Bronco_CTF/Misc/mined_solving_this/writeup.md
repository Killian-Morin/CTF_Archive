# Mined solving this

## Clue / Information

I used to think Minecraft was just a silly game. I woold play it for hours and accomplish nothing. Making this challenge gave me perspective though!

Note: You do not need a copy of Minecraft for this challenge

[world.tar](./world.tar)

## Resolution

After decompressing the archive, I uploaded the folder to [NBT reader online](https://www.brandonfowler.me/nbtreader/) to look for Named Binary Tag that might hold the flag.

Except from the world name/level name which is broncoCTF, the flag does not appear at this step.

However I noticed that the inventory of the player accessed through `Data/Player/Inventory` contains stone and 13 types of wool.
In the description there is `I **woold** play ...` it does not seem to be a typo.

The types of wool present are: red, yellow, lime, green, cyan, lightblue, blue, purple, magenta, pink, orange, brown, black

The white, lightgray and gray wool are missing from the list of all wool types present in Minecraft to this day.

I also used [NBT explorer app](https://github.com/jaquadro/NBTExplorer) but also found nothing with the find tool.

The inventory is like this when first launching the world: [inventory screenshot](./inventory_screenshot.png)

## Writeup

[Mined Solving This - Write-up](https://nacatech.es/writeups/bronco_ctf_25/mined_solving_this/)
