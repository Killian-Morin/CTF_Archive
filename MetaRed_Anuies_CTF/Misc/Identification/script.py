import re

file = open('datos.csv', 'r')

text = file.read()

ID = list()
name = list()
address = list()
phone_number = list()
mail = list()
solde = list()

text = text.split("\n")
print(text[1].split(","))

pattern = re.compile(r"""
    \b(1?[0-9]{1,2}|200)\b\s*,\s*   # ID (1 to 200)
    ([A-Za-zÁÉÍÓÚáéíóúÑñ]+(?:\s+[A-Za-zÁÉÍÓÚáéíóúÑñ]+)*)\s*,\s*  # Nombre (multiple words)
    "([^"]*)"\s*,\s*  # Dirección (enclosed in double quotes)
    (\d{3}[-\s]?\d{3}[-\s]?\d{4})\s*,\s*  # Número de Teléfono
    ([\w\.-]+@[\w\.-]+\.\w{2,})\s*,\s*  # Correo Electrónico
    (\d+(?:\.\d{1,2})?)  # Saldo (integer or decimal number)
""", re.VERBOSE)

for line in text:
    match = pattern.match(line)
    if match:
        print(match.groups())
    else:
        print("no match")
