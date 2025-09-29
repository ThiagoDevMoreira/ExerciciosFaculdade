# Todos os nomes de funções foram mantidos simples, semântios e diretos para representar
# os príncípios pelos quais o Python se fundamenta, além de considerar que a aplicação
# está destinada a entregar uma única solução relativamente simples.
#
# Por isso a preferencia de nomear simplesmente como `media()` em vez de `calcula_media()`,
# além de manter a implementação na forma de encadeamento de funções mais simples de entender,
# que é justamente a abordagem de implementação que escolhi.

# Lista de bimestres para auxiliar na exibição de dados na tela.
bimestre = [
    "Primeiro Bimestre",
    "Segundo Bimestre",
    "Terceiro Bimestre",
    "Quarto Bimestre"
]

# Lista para armazenar as notas no sistema.
lista_de_notas = []

# Validação das notas.
def nota_esta_entre_zero_e_dez(nota):
    return 0 <= nota <= 10

# Implementa o critério de aprovação.
def aluno_esta_aprovado(media):
    return media >= 7

# Apresenta relatório na tela.
def exibir(media):
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    for i in range(len(bimestre)):
        print(f"Nota do {bimestre[i]} : {lista_de_notas[i]}")
    print(".")
    print("A média das notas é: ", media)

    # Deixei a responsabilidade de processar o critério de aprovação numa função separada,
    # assim esta função se mantêm "concentrada" apenas na tarefa de exibir dados na tela.
    if aluno_esta_aprovado(media):
        print("O aluno/a está aprovado/a.")
    else:
        print("O aluno/a está REPROVADO/A.")

# Implementa o cálculo da média das notas
def media(notas):
    return sum(notas) / len(notas)

# Coleta e valida as notas entradas pelo usuário.
def notas():
    for i in range(len(bimestre)):
        while True: # Repete caso não tenha entrado um valor numérico válido
            try:
                print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                nota = float(input(f"Digite a nota do {bimestre[i]}, entre 0.0 e 10.0: "))
                if nota_esta_entre_zero_e_dez(nota):
                    lista_de_notas.append(nota)
                    break
                else:
                    print("A nota deve estar entre 0 (zero) e 10 (dez).")
            except ValueError:
                print("Entrada inválida, digite um número.")
    return lista_de_notas

# Ponto de entrada da aplicação.
# Código pensando para ser chamado com uma única linha de forma semântica sem necessidade
# de conhecer nenhum detalhe de implementação de regras de negócio. Essa é a razão de
# escolher a abordagem de funções em cascada.
if __name__ == "__main__":
    exibir(media(notas()))
