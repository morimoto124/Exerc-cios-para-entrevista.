
#Teste 05


def inverter_string(s):
    nova_string = ''
    for char in s:
        nova_string = char + nova_string
    return nova_string

# Exemplo de uso:
string_original = input("Digite uma string para inverter: ")
string_invertida = inverter_string(string_original)
print("String Invertida:", string_invertida)