# Clue / Information
DEADFACE seems to have gathered information on a pharmaceutical CEO Albert Bourla in an attempt to create a valid work order to Aurora Pharmaceuticals. They claim to have cracked his password by doing a deep dive into his history.

Apparently the password is his dogs names and the day month and year he received “The Golden Cross of the Order of the Redeemer” award and the Year his thesis was published.

Submit the flag as flag{dog1*year$Dog2+MM-dd-YY}

We don't know the order the dogs names are listed, but we are sure the 2nd name starts with a capitol letter.

Submit the flag as flag{flag-text}

# Resolution

Tips: always use google as a search engine to do OSINT, there is always better results.

dogs name: https://www.linkedin.com/posts/albert-bourla_happy-national-pet-day-today-were-giving-activity-7051554863888883712-St5C/
Simba and Charlie

For the Year his thesis was published -> search 'Thesis' in Wikipedia only mention of it followed by the date: 1991
verified on his LinkedIn: https://www.linkedin.com/in/albert-bourla/

For the day month and year he received “The Golden Cross of the Order of the Redeemer”
Wikipedia page -> only mention of it is referenced by https://www.kathimerini.gr/society/561794791/mpoyrla-i-k-sakellaropoyloy-parasimoforise-ton-dieythynonta-symvoylo-tis-pfizer/ the article was published or last edited 05.04.2022

Since Simba is mentionned first I thougth that they would have deliberately place it as second in the flag (and I was right lol)

The flag is: `flag{charlie*1991$Simba+04-05-2022}`
