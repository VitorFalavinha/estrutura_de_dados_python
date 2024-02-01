import re

teste = "Entre em contato, meu email é vitorfala@gmail.com"

print(re.search('\w+@\w+\.\w+', teste))

