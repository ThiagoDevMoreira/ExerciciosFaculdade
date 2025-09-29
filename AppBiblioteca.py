import matplotlib.pyplot as plt
from collections import Counter

## Passo 1: Definir a classe Livro
class Livro:
    def __init__(self, titulo, autor, genero, qtd_disponivel):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.qtd_disponivel = qtd_disponivel

    def __repr__(self):
        return f"Livro(titulo='{self.titulo}', genero='{self.genero}', qtd={self.qtd_disponivel})"

## Adicional ao Passo 1: Classe para gestão da coleção de livros.
# > Responsabilidade única de implementar funcionalidades e não lida com a exibição de dados.
class Biblioteca:
    def __init__(self):
        self.livros = []

    def adiciona_livro(self, livro: Livro) -> bool:
        if isinstance(livro, Livro):
            self.livros.append(livro)
            return True
        return False

    def obtem_todos_os_livros(self) -> list[Livro]:
        return self.livros

    def obtem_livros_por_titulo(self, titulo) -> list[Livro]:
        titulo = titulo.lower()
        return [livro for livro in self.livros if titulo in livro.titulo.lower()]

    def conta_por_genero(self) -> dict:
        #### Retorna dicionário com {genero: quantidade_total}
        contador = Counter()
        for livro in self.livros:
            contador[livro.genero] += 1   # conta 1 título, não qtd_disponivel
        return dict(contador)

class App:
    def __init__(self):
        self.name = "App Biblioteca v0.2"
        self.biblioteca = Biblioteca()
        self.instrucoes = {
            1: "Adicionar livro",
            2: "Listar todos os livros",
            3: "Buscar por título",
            4: "Gráfico de livros por gênero",
            5: "Sair da Biblioteca"
        }
        self.acoes = {
            1: self.opcao_adicionar,
            2: self.opcao_listar,
            3: self.opcao_buscar,
            4: self.opcao_grafico,
            5: self.opcao_sair
        }

        print("📚 Bem-vindo/a à Biblioteca.")

    def obtem_instrucao(self):
        while True:
            print("\nFuncionalidades da Biblioteca:")
            for chave, valor in self.instrucoes.items():
                print(f"[{chave}] {valor}")
            try:
                opcao = int(input("Escolha uma opção (1 a 5): "))
                if opcao in self.instrucoes:
                    return opcao
                else:
                    print("Opção inválida.")
            except ValueError:
                print("Digite apenas números.")

    ### Ações
    def opcao_adicionar(self):
        titulo = input("Título: ")
        autor = input("Autor: ")
        genero = input("Gênero: ")
        qtd = int(input("Quantidade disponível: "))
        livro = Livro(titulo, autor, genero, qtd)
        self.biblioteca.adiciona_livro(livro)
        print("Livro adicionado com sucesso!")

    def opcao_listar(self):
        livros = self.biblioteca.obtem_todos_os_livros()
        if livros:
            print("Livros cadastrados:")
            for l in livros:
                print("-", l)
        else:
            print("Nenhum livro na biblioteca.")

    def opcao_buscar(self):
        termo = input("Digite parte do título: ")
        encontrados = self.biblioteca.obtem_livros_por_titulo(termo)
        if encontrados:
            print("Livros encontrados:")
            for l in encontrados:
                print("-", l)
        else:
            print("Nenhum livro encontrado.")

    def opcao_grafico(self):
        dados = self.biblioteca.conta_por_genero()
        if not dados:
            print("Nenhum livro na biblioteca para gerar gráfico.")
            return

        generos = list(dados.keys())
        quantidades = list(dados.values())

        plt.bar(generos, quantidades, color="skyblue")
        plt.title("Quantidade de Livros por Gênero")
        plt.xlabel("Gênero")
        plt.ylabel("Quantidade")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def opcao_sair(self):
        print("👋 Saindo da Biblioteca. Até mais!")
        exit()

    def executa(self):
        while True:
            instrucao = self.obtem_instrucao()
            acao = self.acoes.get(instrucao)
            if instrucao == 5:
                return acao() # usa `returnr` para interromper o loop para encerrar o app
            if acao:
                acao()

if __name__ == "__main__":
    app = App()
    app.executa()
