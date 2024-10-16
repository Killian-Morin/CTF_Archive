# Clue / Information
A bank analyst is TRYING to IDENTIFY some inconsistencies. Can you help him?

Hint for the flag: flagmx{IDentify}, so need to get the ID

# Resolution
removed all invalid address, just looked for non existent country
then looked for phone number that are of the length (10) and in one string

# writeup
Looking for duplicate data we find 77 and 128 (also 185 but "you didn't need that in any case" even though we have no clue how this one person is not meaningful) have the same address.
The flag is the two IDs ... flagmx{77128}