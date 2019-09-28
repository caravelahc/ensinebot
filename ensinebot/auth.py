import twitter
from pathlib import Path

# Faz a autenticacao na api, pegando as informacoes necessarias de um arquivo ou de input
def auth():

    path = Path('.credentials')

    if path.exists():
        # Se arquivo .credentials existe, as informacoes sao recuperadas dele
        with open(path) as f:
            ck = f.readline()
            cs = f.readline()
            atk = f.readline()
            ats = f.readline()
    else:
        # Caso o arquivo nao exista, as informacoes sao pedidas por input
        print("Arquivo inexistente, autenticacao necessaria:")
        ck = input()
        cs = input()
        atk = input()
        ats = input()

    # Cria o objeto da api com as informacoes necessarias para que se possa ler e postar coisas
    api = twitter.Api(consumer_key=ck,consumer_secret=cs,access_token_key=atk,access_token_secret=ats)
    return api
