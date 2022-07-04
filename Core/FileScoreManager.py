nomeArquivo = 'save/save.txt'

def substituiArquivoTemporario(arquivoOriginal, arquivoTemporario):
	from os import remove, rename
	remove(arquivoOriginal)
	rename(arquivoTemporario, arquivoOriginal)
	return None

def gravaPontuacao(score):
    global nomeArquivo
    
    nomeTemp = nomeArquivo + "temp"
    temp = open(nomeTemp, "w+")
    
    currentScore = obterPontuacao()
    
    inserted = False
    for i in range(len(currentScore)):
        if(int(currentScore[i][1]) < score[1]):
            currentScore.insert(i, score)
            inserted = True
            break
    
    if not inserted:
        currentScore.append(score)
    
    for i in range(0, len(currentScore)):
        if i <= 5:
	        text = f'{currentScore[i][0]}={currentScore[i][1]}'
        	temp.write(text + '\n')
    
    temp.close()
    substituiArquivoTemporario(nomeArquivo, nomeTemp)
    return None

def obterPontuacao():
    global nomeArquivo
    
    currentScore = []
    
    try:
    	file = open(nomeArquivo, "r")
    except:
        file = open(nomeArquivo, 'w+')
    
    for line in file:
        lineScore = line.split('=')
        currentScore.append((lineScore[0], lineScore[1][0:-1]))
    file.close()
    
    return currentScore