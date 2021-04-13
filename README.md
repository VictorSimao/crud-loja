# crud-loja

## Solução

A solução adotada foi:
```Python
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
```

## Explicação

Dada a alteração da estrutura base para acesso ao processo, por meio da main.py, que está situada na pasta app, fora do escopo raiz, a solução usada atende corretamente a esta mudança. Além disso, é tida como uma recomendação muito popular, neste tipo de caso.

## Diferenças entre caminho relativo e absoluto

- Um caminho absoluto (completo) expressa exatamente a localização em um sistema de arquivos, a partir do diretório raiz, independentemente do diretório de trabalho atual.

- Um caminho relativo indica a localização parcial do arquivo.
