def matriz3d(matriz, n):
    lista_pos =[]
    for ind_linha, linha in enumerate(matriz):
        for ind_coluna, coluna in enumerate(linha):
            if coluna == n:
                lista_pos.append((ind_linha, ind_coluna))
    return lista_pos

def aluno(ra, n):
	
	convert_string = str(ra)
	meu_array = str(ra)+convert_string[0:2]
	lista = [int(a) for a in str(meu_array)]
	matriz = []
	while lista != []:
	    matriz.append(lista[:3])
	    lista = lista[3:]
    
	return matriz3d(matriz,n)
	
ra = input('Digite o seu ra.')
n = int(input('Digite o valor a ser localizado.'))
print(aluno(ra,n))