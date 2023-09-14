import csv

# Defina o nome do arquivo CSV de entrada
arquivo_csv = 'resultado.csv'

# Dicionário para armazenar as notas dos alunos
notas_alunos = {}

# Lê o arquivo CSV
with open(arquivo_csv, 'r') as arquivo:
    leitor_csv = csv.reader(arquivo)
    
    # Lê o gabarito da primeira linha
    gabarito = next(leitor_csv)
    
    # Loop pelas linhas do CSV
    for linha in leitor_csv:
        matricula, nome, respostas = linha[0], linha[1], linha[2:]
        
        # Calcula a nota do aluno
        nota = sum([1 for i, resposta_aluno in enumerate(respostas) if resposta_aluno == gabarito[i + 2]])
        
        # Armazena a nota do aluno no dicionário
        notas_alunos[nome] = nota

# Encontra o aluno com a maior nota
aluno_maior_nota = max(notas_alunos, key=notas_alunos.get)
maior_nota = notas_alunos[aluno_maior_nota]

# Encontra o aluno com a menor nota
aluno_menor_nota = min(notas_alunos, key=notas_alunos.get)
menor_nota = notas_alunos[aluno_menor_nota]

# Calcula a média das notas
media_notas = sum(notas_alunos.values()) / len(notas_alunos)

# Cria um arquivo CSV chamado "tabela_notas" para armazenar os resultados
with open('tabela_notas.csv', 'w', newline='') as arquivo_saida:
    escritor_csv = csv.writer(arquivo_saida)
    
    # Escreve os cabeçalhos no arquivo de saída
    escritor_csv.writerow(['Nome', 'Nota'])
    
    # Escreve as informações da maior e menor nota no arquivo
    escritor_csv.writerow(['Maior Nota', aluno_maior_nota, maior_nota])
    escritor_csv.writerow(['Menor Nota', aluno_menor_nota, menor_nota])
    escritor_csv.writerow(['Média Notas', '', media_notas])
    
    # Escreve as notas de todos os alunos no arquivo
    for nome, nota in notas_alunos.items():
        escritor_csv.writerow([nome, nota])
