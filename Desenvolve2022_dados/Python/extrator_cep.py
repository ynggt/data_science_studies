import re

endereco = "Rua Jardim das Rosídeas 78, bairro Santa Maria, Espírito Santo, ES, 10313-091"


# Importando Regular Expression -- RegEx

padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")
busca = padrao.search(endereco)     # SEARCH buscando dentro de uma string um certo padrão
if busca:
    cep = busca.group()
    print(cep)

