
"""Exibe relatório de crianças por atividade.

imprime a lista de crianças agrupadas por sala que frequentam cada uma das atividades.
"""

__version__ = "0.1.0"

# Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]
aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("Inglês",aula_ingles),
    ("Música",aula_musica),
    ("Dança",aula_danca),
     
]

for nome_atividade, atividade in atividades:
    print(f"Alunos da atividade {nome_atividade}")
    print("_" * 30,"\n")

    # aula_sala1 = [aluno for aluno in atividade if aluno in sala1]
    # aula_sala2 = [aluno for aluno in atividade if aluno in sala2]

    aula_sala1 = set(sala1) & set(atividade)
    aula_sala2 = set(sala2) & set(atividade)
    
    print(nome_atividade, "sala 1:", aula_sala1)
    print(nome_atividade, "sala 2:", aula_sala2) 
    print("\n")
    print("#" * 30)
    print("\n")
 