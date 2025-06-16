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
    def __init__(self, titulo, ano_publicacao, disponivel: bool = False):
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
            self.disponivel = True

    def obter_info(self):
        print(f"Nome: {self.titulo} -- Ano Publicação: {self.ano_publicacao} -- Disponível: {ItemBiblioteca.transformar_disponivel(self)}")
        for index, livro in enumerate(self.lista_livro):
            print(f"{index+1}° livro: {livro.titulo}")

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
        print(f"Nome: {self.titulo} -- Ano Publicação: {self.ano_publicacao}-- Disponível: {ItemBiblioteca.transformar_disponivel(self)} -- Número da Edição: {self.numero_edicao}")

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
        print("Segue abaixo a listagem dos itens da biblioteca:")
        for chave in self.itens.keys():
            print(f"- {chave}")




item01 = ItemBiblioteca("1984", 1936,True)
item02 = ItemBiblioteca("Sapiens", 2010,True)
revista01 = Revista("Avengerns", 2001, 12, True)
colecao = ColecaoLivros("Meus Favoritos", "2014")
colecao.adicionar_livro(item01)
colecao.adicionar_livro(item02)

itens = Biblioteca()
itens.adicionar_item(item01)
itens.adicionar_item(item02)
itens.adicionar_item(revista01)
itens.adicionar_item(colecao)
itens.listar_itens_disponiveis()

itens.deletar_item("Sapiens")
itens.listar_itens_disponiveis()