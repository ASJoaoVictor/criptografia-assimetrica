from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import hashlib
from zipfile import ZipFile
from pathlib import Path

caminho = Path(__file__).resolve().parent

def gerar_chaves():
    chave = RSA.generate(1024)
    chave_privada = chave.export_key()
    chave_publica = chave.publickey().export_key()

    with open(f"{caminho.parent}/public.pem", "wb") as a:
        a.write(chave_publica)

    with open(F"{caminho}/private.pem", "wb") as a:
        a.write(chave_privada)

def descompactar():
    with ZipFile(f"{caminho.parent}/package.zip", "r") as a:
        a.extractall(f"{caminho}/extracted")

def calcular_hash_atual():
    with open(f"{caminho}/extracted/texto.txt", "r", encoding="utf-8") as a:
            mensagem = a.read()
    
    return hashlib.sha256(mensagem.encode("utf-8")).hexdigest()

def descriptografar():
    chave_privada = ""
    with open(f"{caminho}/private.pem", "rb") as a:
        chave_privada = a.read()

    chave_privada_obj = RSA.import_key(chave_privada)
    decifra = PKCS1_OAEP.new(chave_privada_obj)

    with open(f"{caminho}/extracted/novotexto.txt", "rb") as a:
        mensagem = a.read()

    return decifra.decrypt(mensagem).decode("utf-8")

def validar_auntenticidade():
    hash_atual = calcular_hash_atual()
    hash_doc = descriptografar()

    if(hash_atual == hash_doc):
        return "Arquivo Auntêntico"
    return "Arquivo não Autêntico"

if __name__ == "__main__":

    while(True):

        print("""1- Gerar Chaves
2- Descompactar
3- Validar arquivo
4- Sair
""")
        operacao = int(input("Selecione a operação: "))

        if(operacao == 4):
            break
        elif(operacao == 1):
            try:
                gerar_chaves()
                print("Chaves geradas")
            except:
                print("Erro gerar chaves, tente novamente!")
        elif(operacao == 2):
            try:
                descompactar()
                print("Arquivos extraídos")
            except:
                print("Erro ao descompactar, tente novamente!")
        elif(operacao == 3):
            try:
                resposta = validar_auntenticidade()
                print(resposta)
            except:
                print("Erro a validar, tente novamente")
            break
