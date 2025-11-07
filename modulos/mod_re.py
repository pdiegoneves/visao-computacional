import re

text = "Udemy - uma plataforma com muitos cursos"


match = re.search(r'uma plataforma', text)
print("Indice inicial: ", match.start())
print("Indice final: ", match.end())

site = "https://www.udemy.com"
match = re.search(r'\.', site)
print(match)

pattern = "[a-m]"
result = re.findall(pattern, text)
print(result)

rule = r'^A'

phrases = ['A casa está suja', 'O dia está lindo', 'Vamos passear!']

for phrase in phrases:
    if re.match(rule, phrase):
        print(phrase, " -> [x] começa com A")
    else:
        print(phrase, " -> [ ] não começa com A")

rule_end = r'!$'
for phrase in phrases:
    if re.search(rule_end, phrase):
        print(phrase, " -> [x] termina com !")
    else:
        print(phrase, " -> [ ] não termina com !")

