# Clue / Information
My brother deleted an important file from the encrypt-decrypt-file repository

# resolution by Theo
Apres telechargement du dossier -> Il sagit d'un projet Mercurial avec un dossier .hg
- Il sagit d'un gestionaire de projet comme git -> donc il y a une command "hg log" apres installer le programme mercurial.
- dans le log il y a un identifiant de commit
- dans le fichier ./.hg/store/data/ il y a les deux anciens fichier illisible dont un fichier main.py.i et un fichier flag.enc.i
- Avec cela on sait que l'on doit revert le commit en recuperant le fichier flag.enc
- La command : hg revert -r "commit value" flag.enc permet de recuperer le fichier
- Ensuite il suffit d'applique la command du main.py avec : python3 main.py --decrypt --input flag.enc --output out.log
- Apres hexdump du fichier out.log il content les caracteres PNG au debut ce qui implique qu'il doit etre renomer en .png
- Apres ouverture du fichier out.png - Le flag apparait