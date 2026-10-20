# 05/02/2026

class Usuario:
    def __init__(self):
        self._id = None
        self._nome = None
        self._email = None
        self._data_criacao = None

    @property
    def id(self):
        return self._id
        
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nome(self):
        return self._nome
        
    @nome.setter
    def nome(self, nome):
        if not nome:
            raise ValueError('Você não pode ter 1 nome vazio.')
        self._nome = nome

    @property
    def email(self):
        return self._email
        
    @email.setter
    def email(self, email):
        self._email = email

    @property
    def data_criacao(self):
        return self._data_criacao
        
    @data_criacao.setter
    def data_criacao(self, data_criacao):
        self._data_criacao = data_criacao

class Permissao:
    def __init__(self):
        self._id = None
        self._descricao = None

    @property
    def id(self):
        return self._id
        
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def descricao(self):
        return self._descricao
        
    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao

class UsuarioPermissao:
    def __init__(self,usuario, permissao):
        self.usuario = usuario 
        self.permissao = permissao

usuario1 = Usuario()
usuario1.id = 1
usuario1.nome =  'Alice Silva'
usuario1.email = 'alice.silva@email.com'
usuario1.data_criacao = '2023-10-01'

usuario2 = Usuario()
usuario2.id = 2
usuario2.nome =  'Bruno Oliveira'
usuario2.email = 'bruno.oliveira@email.com'
usuario2.data_criacao = '2023-10-02'

usuario3 = Usuario()
usuario3.id = 3
usuario3.nome =  'Carla Pereira'
usuario3.email = 'carla.pereira@email.com'
usuario3.data_criacao = '2023-10-03'

usuario4 = Usuario()
usuario4.id = 4
usuario4.nome =  'Daniel Costa'
usuario4.email = 'daniel.costa@email.com'
usuario4.data_criacao = '2023-10-04'

usuario5 = Usuario()
usuario5.id = 5
usuario5.nome =  'Elisa Martins'
usuario5.email = 'elisa.martins@email.com'
usuario5.data_criacao = '2023-10-05'

usuarios = [usuario1, usuario2, usuario3, usuario4, usuario5]

ultimos = sorted(
    usuarios,
    key= lambda usuario: usuario.data_criacao,
    reverse=True
)

ultimos[0].nome = 'novo_nome'




