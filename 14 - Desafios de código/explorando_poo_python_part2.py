# TODO: Crie a classe PlanoTelefone, seu método de inicialização e encapsule os atributos 'nome' e 'saldo':
class PlanoTelefone:
    def __init__(self, nome, saldo):
        self.__nome = nome
        self.__saldo = saldo
    
    # Método para verificar o saldo do plano
    def verificar_saldo(self):
        if self.__saldo < 10:
            return "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif self.__saldo >= 50:
            return "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

    # Método getter para obter o saldo
    def get_saldo(self):
        return self.__saldo


# Classe UsuarioTelefone:
class UsuarioTelefone:
    def __init__(self, nome, plano):
        self.nome = nome  # Nome do usuário
        self.plano = plano  # Plano associado ao usuário

    # Método para verificar o saldo do usuário e gerar a mensagem personalizada
    def verificar_saldo(self):
        saldo = self.plano.get_saldo()  # Acessando o saldo do plano
        mensagem = self.plano.verificar_saldo()  # Obtendo a mensagem personalizada com base no saldo
        return saldo, mensagem  # Retornando o saldo e a mensagem


# Recebendo as entradas do usuário (nome, plano, saldo):
nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())

# Criação de objetos do plano de telefone e usuário de telefone com dados fornecidos:
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial) 
usuario = UsuarioTelefone(nome_usuario, plano_usuario)

# Chamada do método para verificar_saldo e exibir a mensagem personalizada:
saldo_usuario, mensagem_usuario = usuario.verificar_saldo()
print(mensagem_usuario)