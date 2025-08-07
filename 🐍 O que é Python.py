# Python é uma linguagem de programação de alto nível, interpretada, de tipagem dinâmica e multiparadigma (suporta programação orientada a objetos, funcional e imperativa). É conhecida por sua sintaxe clara e legível, o que a torna ideal tanto para iniciantes quanto para profissionais.

#TODO: 🔹 Fundamentos da Linguagem
#* 1. Sintaxe Básica

print("Olá, mundo!")

# Não exige ponto e vírgula. Indentação é obrigatória e define blocos de código.

#* 2. Tipos de Dados

# Numéricos: int, float, complex
x = 10          # int
y = 3.14        # float 
z = 1 + 2j     # complex

# Texto: str
nome = "Python"  # str

# Booleanos: bool
verdadeiro = True  # bool
falso = False      # bool

# Coleções: list, tuple, set, dict
lista = [1, 2, 3]          # list
tupla = (1, 2, 3)          # tuple
conjunto = {1, 2, 3}      # set
dicionario = {"um": 1, "dois": 2, "tres": 3}  # dict

#* 3. Controle de Fluxo

if x > 0:
    print("Positivo")
elif x == 0:
    print("Zero")
else:
    print("Negativo")

#* 4. Laços

for i in range(5):
    print(i)

while x < 10:
    x += 1
    print(x)

#* 5. Funções

def saudacao(nome):
    return f"Olá, {nome}!"
print(saudacao("Mundo"))


#TODO: 🔹 Programação Orientada a Objetos (POO)

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Sou {self.nome} e tenho {self.idade} anos.")
p1 = Pessoa("Alice", 30)
p1.apresentar()

#TODO:🔹 Funções Avançadas

#* 1. Funções Lambda
dobro = lambda x: x * 2
print(dobro(5))  # Saída: 10

#* 2. Decoradores
def log(func):
    def wrapper():
        print("Executando função...")
        func()
    return wrapper

@log
def minha_funcao():
    print("Função executada.")

#* 3. Geradores
def contador():
    for i in range(5):
        yield i
for numero in contador():
    print(numero)
    
#TODO: 🔹 Manipulação de Arquivos

with open("arquivo.txt", "r") as f:
    conteudo = f.read()
    print(conteudo)

#TODO: 🔹 Tratamento de Exceções

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: divisão por zero.")
finally:
    print("Fim do bloco try.")

#TODO: 🔹 Bibliotecas Populares
# NumPy: operações matemáticas e vetoriais
# Pandas: análise de dados
# Matplotlib / Seaborn: visualização
# Scikit-learn: machine learning
# Flask / Django: desenvolvimento web
# Requests / BeautifulSoup: web scraping
# PyTorch / TensorFlow: deep learning

#TODO:🔹 Tópicos Avançados

#* 1. Programação Assíncrona
import asyncio

async def tarefa():
    print("Início")
    await asyncio.sleep(1)
    print("Fim")
asyncio.run(tarefa())


#* 2. Metaprogramação
# Manipulação de código como dados, uso de type(), getattr(), setattr().

#* 3. Design Patterns
# Aplicação de padrões como Singleton, Factory, Observer, etc.

#* 4. Testes Automatizados
import unittest

class Teste(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(1 + 1, 2)
if __name__ == "__main__":
    unittest.main()
    
#TODO🔹 Ambientes e Ferramentas
# Jupyter Notebook: ideal para ciência de dados
# VS Code / PyCharm: IDEs poderosas
# pip / conda: gerenciamento de pacotes
# venv / poetry: ambientes virtuais