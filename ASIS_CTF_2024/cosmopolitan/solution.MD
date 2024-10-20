- faire un `hexdump -C` ou juste `vim` le .pdf

- avant le HEADER `PDF` il y a des caractères non-imprimables
	- ces caractères empêchent la bonne execution de `gs` (Ghostscript (PostScript and PDF language interpreter and previewer)) et d'autres outils

- les 4 premiers bits de ces caractères non-imprimables donnent: ico
https://en.wikipedia.org/wiki/List_of_file_signatures
`00 00 01 00` = Computer icon encoded in ICO file format

- si on renomme le `.pdf` en un fichier `.ico` alors le flag est donné