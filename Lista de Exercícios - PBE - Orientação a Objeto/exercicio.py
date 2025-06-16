# Classe Item Biblioteca - Classe Pai
class ItemBiblioteca:
    def __init__(self, titulo, ano_publicacao, disponivel):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.disponivel = disponivel

    def emprestar(self):
        if self.disponivel:
            print("O livro está disponível para empréstimo, é possível realizar sua retirada.")
            self.disponivel = False
        else:
            print("O livro não está disponível para empréstimo.")

    def devolver(self):
        if not self.disponivel:
            print("Livro devolvido com sucesso")
            self.disponivel = True
        else:
            print("Esse item não está com você, ele está disponível para retirada na biblioteca.")

    def transformar_disponivel(self):
        if self.disponivel:
            disponivel = "Sim"
        else:
            disponivel = "Não"
        return disponivel

    def obter_info(self):
        print(f"Título: {self.titulo} -- Ano Publicação: {self.ano_publicacao} -- Disponível: {ItemBiblioteca.transformar_disponivel(self)}")

# Classe Coleção de livros - Classe Filha
class ColecaoLivros(ItemBiblioteca):
    def __init__(self, titulo, ano_publicacao, disponivel: bool = True):
        super().__init__(titulo, ano_publicacao, disponivel)
        self.lista_livro = []

    def adicionar_livro(self, livro: ItemBiblioteca):
        self.lista_livro.append(livro)
        return  self.lista_livro

    def verificar_disponibilidade(self):
        for livro in self.lista_livro:
            if not livro.disponivel:
                self.disponivel = False
                break

    def obter_info(self):
        print(f"Coleção; Nome: {self.titulo} -- Ano Publicação: {self.ano_publicacao} -- Disponível: {ItemBiblioteca.transformar_disponivel(self)}")

# Classe Revista - Classe Filha
class Revista(ItemBiblioteca):
    def __init__(self, titulo, ano_publicacao, numero_edicao, disponivel: bool = False):
        super().__init__(titulo, ano_publicacao, disponivel)
        self.numero_edicao = numero_edicao

    def atualizar_edicao(self, nova_edicao):
        if nova_edicao < 0:
            raise ValueError("O número da nova edição não pode ser menor que 0")
        self.numero_edicao = nova_edicao

    def restringir_emprestimo(self, dias_max):
        if self.ano_publicacao < 2000 and dias_max > 7:
            return False
        else:
            return True

    def obter_info(self):
        print(f"Revista; Nome: {self.titulo} -- Ano Publicação: {self.ano_publicacao}-- Disponível: {ItemBiblioteca.transformar_disponivel(self)} -- Número da Edição: {self.numero_edicao}")

# Classe Biblioteca - Lista de itens da biblioteca
class Biblioteca:
    def __init__(self):
        self.itens = {}

    def adicionar_item(self, item: ItemBiblioteca):
        if item.titulo in self.itens.values():
            raise ValueError("Esse item já existe na biblioteca!")
        else:
            self.itens[item.titulo] = item

    def deletar_item(self, titulo):
        if titulo in self.itens:
            del self.itens[titulo]
            print("Item removido da biblioteca!")
        else:
            print("O item não está contido na biblioteca!")

    def listar_itens_disponiveis(self):
        print("Segue abaixo a listagem dos itens disponíveis da biblioteca:")
        titulos_disponiveis = []
        for titulo, item in self.itens.items():
            if item.disponivel:
                titulos_disponiveis.append(titulo)
        print(f"- {titulos_disponiveis}")

    def contar_item_emprestados(self):
        qtd = 0
        for titulo in self.itens.values():
            if not titulo.disponivel:
                qtd += 1
        return qtd

# Classe RelatorioBiblioteca - Gera um relat[orio completo sobre a biblioteca
class RelatorioBiblioteca:
    def __init__(self, biblioteca: Biblioteca):
        self.relatorio = biblioteca

    def gerar_relatorio_completo(self):
        print("\nRelatório completo: ")
        for item in self.relatorio.itens.values():
            item.obter_info()

    def gerar_relatorio_disponibilidade(self):
        print("\nSegue abaixo os itens disponíveis da biblioteca: ")
        i = 0
        for item in self.relatorio.itens.values():
            if item.disponivel:
                print(f"- {item.titulo}")
                i += 1
        print(f"Existem {i} itens disponíveis na biblioteca.")

    def gerar_relatorio_emprestimos(self):
        print("\nSegue abaixo a quantidade de itens emprestados: ")
        total = len(self.relatorio.itens)
        itens_emprestados = 0
        for item in self.relatorio.itens.values():
            if not item.disponivel:
                itens_emprestados += 1
        print(f"{itens_emprestados} de {total} itens estão emprestados! ({itens_emprestados*100/total:.2f}%)")


item01 = ItemBiblioteca("1984", 1936,True)
item02 = ItemBiblioteca("Sapiens", 2010,True)
item03 = ItemBiblioteca("Diário de um Banana", 2017, False)
revista01 = Revista("Avengerns", 2001, 12, True)
revista02 = Revista("Demolidor", 2010, 5, False)
colecao = ColecaoLivros("Meus Favoritos", "2014")

colecao.adicionar_livro(item01)
colecao.adicionar_livro(item02)
colecao.verificar_disponibilidade()

itens = Biblioteca()
itens.adicionar_item(item01)
itens.adicionar_item(item02)
itens.adicionar_item(item03)
itens.adicionar_item(revista01)
itens.adicionar_item(revista02)
itens.adicionar_item(colecao)

RelatorioBiblioteca(itens).gerar_relatorio_completo()
RelatorioBiblioteca(itens).gerar_relatorio_disponibilidade()
RelatorioBiblioteca(itens).gerar_relatorio_emprestimos()