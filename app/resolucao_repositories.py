"""
O módulo sys.path contém uma lista de strings que determina caminhos de busca conhecidos pelo interpretador do Python. Este é iniciade por um caminho padrão, determinado pela vaviárel de ambiente PYTHONPATH. É possível definir um valor para tal. 
No caso, o Pytho, por padrão, inicia buscando um módulo e, caso não encontrar, busca por um arquivo .py com o mesmo nome, dentro do próprio diretório em que está sendo executado. Caso o módulo desejado esteja em um diretŕio diferente do atual, será preciso acrescentar na variável de ambiente PYTHONPATH o caminho que precisa percorrer (caminho absoluto), usando path.abspath(__file__). 

import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

Referências:

https://docs.python.org/pt-br/3/tutorial/modules.html#tut-standardmodules

https://docs.python.org/pt-br/3/library/sys.html#sys.path

"""