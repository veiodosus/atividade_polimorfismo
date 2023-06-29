class Cliente:

    def __init__(self, cpf: str, nome: str, idade: int):
        self.__cpf = cpf
        self.__nome = nome
        self.__idade = idade

    def mais_idade(self, valor):
        self.__idade += valor

    def mais_nome(self, caracteres):
        self.__nome += caracteres

    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    def __str__(self) -> str:
        return f'CPF: {self.__cpf}\t| NOME: {self.__nome}\t| IDADE: {self.__idade}'

class Seguro:

    def __init__(self, num_apolice: int, proprietario: Cliente):
        self._num_apolice = num_apolice
        self._propietario = proprietario
        self._valor = 0
        self._premio = 0
    
    def calcular_valor(self):
        pass

    def calcular_premio(self):
        pass

    def __str__(self):
        return f'NUMERO DE APOLICE: {self._num_apolice}\t| PROPRIETARIO: {self._propietario.nome}\t| PREMIO: {self._premio}\t| VALOR: {self._valor:.2f}'

class Seguro_Vida(Seguro):

    def __init__(self, num_apolice: int, propietario: Cliente, nome_beneficiario: str, duracao: int):
        super().__init__(num_apolice, propietario)
        self.__nome_beneficiario = nome_beneficiario
        self.__duracao = duracao

    @property
    def nome_beneficiario(self):
        return self.__nome_beneficiario

    @property
    def duracao(self):
        return self.__duracao

    def calcular_valor(self):
        if self.__duracao < 31:
            self._valor = 800
            return 800
        elif self.__duracao < 51:
            self._valor = 1300
            return 1300
        else:
            self._valor = 1600
            return 1600

    def calcular_premio(self):
        if self.__duracao < 31:
            self._premio = 50000
            return 50000
        elif self.__duracao < 51:
            self._premio = 30000
            return 30000
        else:
            self._premio = 20000
            return 20000

class Seguro_Automovel(Seguro):

    def __init__(self, num_apolice: int, proprietario: Cliente, num_licenca: int, nome_modelo: str, ano: int, valor_automovel: float):
        super().__init__(num_apolice, proprietario)
        self.__num_licenca = num_licenca
        self.__nome_modelo = nome_modelo
        self.__ano = ano
        self.__valor_automovel = valor_automovel
        self.__franquia = 0

    @property
    def num_licenca(self):
        return self.__num_licenca

    @property
    def nome_modelo(self):
        return self.__nome_modelo

    @property
    def ano(self):
        return self.__ano
    
    @property
    def valor_automovel(self):
        return self.__valor_automovel

    @property
    def franquia(self):
        return self.__franquia

    def calcular_valor(self):
        self._valor = self.__valor_automovel / 100 * 3

    def calcular_premio(self):
        self._premio = self.__valor_automovel / 100 * 80

    def calcular_franquia(self):
        self.__franquia = self._valor / 100 * 40

class Controle_Seguros:

    def __init__(self):
        self.__seguros = []
        self.__qtd_vida = 0
        self.__qtd_auto = 0

    @property
    def seguros(self):
        return self.__seguros

    def cadastrar_seguro_vida(self, seguro: Seguro_Vida):
        seguro.calcular_premio()
        seguro.calcular_valor()
        
        self.__seguros.append(seguro)
        self.__qtd_vida += 1

    def cadastrar_seguro_automovel(self, seguro: Seguro_Automovel):
        seguro.calcular_premio()
        seguro.calcular_valor()
        seguro.calcular_franquia
        self.__seguros.append(seguro)
        self.__qtd_auto += 1

    def cadastrar_seguro(self, seguro):
        if type(seguro) == Seguro_Vida:
            self.cadastrar_seguro_vida(seguro)
        else:
            self.cadastrar_seguro_automovel(seguro)

    def relatorio_seguros(self):
        valor_total = 0
        for n in self.__seguros:
            valor_total += n._valor
            print(f'\n{n}')
        print(f'\nSEGUROS DE VIDA: {self.__qtd_vida}\nSEGUROS DE AUTOMÓVEIS: {self.__qtd_auto}')
        print(f'\nVALOR TOTAL: {valor_total:.2f}')
"""CONTROLE DE SEGUROS"""
controle = Controle_Seguros()
"""CLIENTES"""
cliente_1 = Cliente(12345678900, 'Jorge', 35)
cliente_2 = Cliente(78945612300, 'Marcelo', 19)
cliente_3 = Cliente(98765432100, 'Marcia', 25)
cliente_4 = Cliente(32165498700, 'Eduardo', 40)
cliente_5 = Cliente(00000000000, 'Gustavo', 50)
"""SEGUROS DE VIDA"""
seguro_de_vida_1 = Seguro_Vida(1, cliente_1, 'Jorge', 50)
seguro_de_vida_2 = Seguro_Vida(2, cliente_2, 'Marcelo', 60)
seguro_de_vida_3 = Seguro_Vida(3, cliente_3, 'Marcia', 30)
seguro_de_vida_4 = Seguro_Vida(4, cliente_4, 'Eduardo', 45)
seguro_de_vida_5 = Seguro_Vida(5, cliente_5, 'Gustavo', 20)
"""SEGURO DE AUTOMÓVEIS"""
seguro_de_automovel_1 = Seguro_Automovel(6, cliente_1, 123, 'Uno', 2010, 50000.00)
seguro_de_automovel_2 = Seguro_Automovel(7, cliente_3, 321, 'Veloster', 2016, 90000.00)
seguro_de_automovel_3 = Seguro_Automovel(8, cliente_5, 456, 'Celta', 2000, 20000.00)
"""CADASTRAMENTO DE SEGUROS"""
controle.cadastrar_seguro(seguro_de_vida_1)
controle.cadastrar_seguro(seguro_de_vida_2)
controle.cadastrar_seguro(seguro_de_vida_3)
controle.cadastrar_seguro(seguro_de_vida_4)
controle.cadastrar_seguro(seguro_de_vida_5)
controle.cadastrar_seguro(seguro_de_automovel_1)
controle.cadastrar_seguro(seguro_de_automovel_2)
controle.cadastrar_seguro(seguro_de_automovel_3)
"""RELATÓRIO"""
controle.relatorio_seguros()