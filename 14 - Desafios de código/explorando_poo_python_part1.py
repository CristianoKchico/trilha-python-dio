# TODO: Crie uma classe UsuarioTelefone.  
class UsuarioTelefone:
# TODO: Defina um método especial `__init__`, que é o construtor da classe.
# O método `__init__`, irá inicializar os atributos da classe: `nome`, `numero` e `plano`.
  def __init__(self, nome, numero, plano):
    # TODO: Aplique o conceito de encapsulamento, onde os atributos serão encapsulados dentro da classe.
    self.__nome = nome
    self.__numero = numero
    self.__plano = plano

      
    # A classe `UsuarioTelefone` define um método especial `__str__`, que retorna uma representação em string do objeto.
  def __str__(self):
      return f"Usuário {self.__nome} criado com sucesso."

def main():
# Entrada:
  nome = input("Digite o nome de usuário: ")  
  numero = input("Digite o Número: ")  
  plano = input("Escolha seu pano: ")
  
# TODO: Crie um novo objeto `UsuarioTelefone` com os dados fornecidos:
  usuario = UsuarioTelefone(nome, numero, plano)
  print(usuario)

main()