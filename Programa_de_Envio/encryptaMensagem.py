from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import hashlib
from zipfile import ZipFile
from pathlib import Path

caminho = Path(__file__).resolve().parent

def encryptar(mensagem):
    chave_publica = ""
    with open(f"{caminho.parent}/public.pem", "rb") as a:
        chave_publica = a.read()

    chave_publica_obj = RSA.import_key(chave_publica)
    cifra = PKCS1_OAEP.new(chave_publica_obj)

    mensagem = mensagem.encode("utf-8")
    
    return cifra.encrypt(mensagem)

def gerar_hash_mensagem(mensagem):
    return hashlib.sha256(mensagem.encode("utf-8")).hexdigest()

def gerar_hash_arquivo(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as a:
        mensagem = a.read()

    return gerar_hash_mensagem(mensagem)


def encryptar_mensagem():
    with open(f"{caminho}/novotexto.txt", "wb") as a:
        a.write(encryptar(gerar_hash_arquivo(f"{caminho}/texto.txt")))

    return True;

        
def compactar_arquivo():
    with ZipFile(f"{caminho.parent}/package.zip", "w") as a:
        a.write(f"{caminho}/novotexto.txt", arcname="novotexto.txt")
        a.write(f"{caminho}/texto.txt", arcname="texto.txt")

    return True


if __name__ == "__main__":
    while(True):
        print("""1- Criar mensagem para enviar
2- encriptar mensagem
3- Compactar mensagem
4- Sair
""")

        operacao = int(input("Digite o número da operação: "))

        if(operacao == 4):
            break
        elif(operacao == 1):
            try:
                mensagem = str(input("Digite a mensagem para ser enviada: "))
                with open(f"{caminho}/texto.txt", "w") as a:
                    a.write(mensagem)
                print("Documento criado")
            except:
                print("Erro ao criar documento")
        elif(operacao == 2):
            try:
                encryptar_mensagem()
                print("Mensagem encriptada com sucesso")
            except:
                print("Erro ao encriptar mensagem, tente novamente!")
        elif(operacao == 3):
            try:
                compactar_arquivo()
                print("Arquivos compactados com sucesso!")
                break
            except:
                print("Erro ao compactar arquivo, tente novamente!")