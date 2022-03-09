##Exemplos de URLs válidas:
import re

''''' bytebank.com/cambio
 bytebank.com.br/cambio
 www.bytebank.com/cambio
 www.bytebank.com.br/cambio
 http://www.bytebank.com/cambio
 http://www.bytebank.com.br/cambio
 https://www.bytebank.com/cambio
 https://www.bytebank.com.br/cambio''''''''

##Exemplos de URLs inválidas:
    https://bytebank/cambio
    https://bytebank.naoexiste/cambio
    ht://bytebank.naoexiste/cambio'''''


## URL's para teste
url1 = 'https://www.bytebank.com/cambio'
url2 = 'https://bytebank/cambio'
url3 = 'bytebank.com.br/cambio'
url4 = 'https://bytebank.naoexiste/cambio'


padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padrao_url.match(url4) ## Método MATCH verifica se são exatamente iguais
#método match retorna None ou um Match

if not match:
    raise ValueError("A URL não é válida")
else:
    print("A URL é válida")
