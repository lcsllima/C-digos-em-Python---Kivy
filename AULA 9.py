frase = "ABCDEFGH IJKLMN"
frase2 = "oo c ppp aaaaa o cccc a"
frase3 = "       ola      :        "
print(frase[3:7:2])
print(frase[:7])
print(frase[7:])
print(frase[4::5])
print(frase2.count("a"))
print(frase2.count("a",12,23))
print(frase2.find("ppp"))
print("o" in frase2)
print(frase2.replace("aaaaa","substituto"))
print(frase2.upper())
print(frase.lower())
print(frase2.capitalize())
print(frase2.title())
print(frase3.strip())
print(frase3.lstrip())
print(frase3.rstrip())
print(frase3.split())
print("-".join(frase3))