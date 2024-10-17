# Calculadora Simples

Uma calculadora simples implementada em Python com operações básicas.

## Instalação

Você pode instalar este pacote usando pip:

pip install calculadora_simples
## Uso

Aqui está um exemplo de como usar a calculadora:

```python
from calculadora_simples import Calculadora

calc = Calculadora()

print(calc.adicionar(2, 3))  # Saída: 5
print(calc.subtrair(5, 3))   # Saída: 2
print(calc.multiplicar(2, 3))  # Saída: 6
print(calc.dividir(6, 2))    # Saída: 3.0
DesenvolvimentoPara configurar o ambiente de desenvolvimento:
Clone o repositório
Instale as dependências: pip install -r requirements.txt
Execute os testes: python -m unittest discover tests