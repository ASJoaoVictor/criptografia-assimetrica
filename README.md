# Criptografia Assimetrica

Este projeto demonstra o uso de criptografia assimetrica com RSA e integridade por meio de hash SHA-256.

O programa [chaves.py](Programa_de_Gerenciamento/chaves.py) gera o par de chaves e valida os arquivos recebidos. O programa [encryptaMensagem.py](Programa_de_Envio/encryptaMensagem.py) cria uma mensagem, gera o hash dessa mensagem, cifra o hash e compacta os arquivos para envio.

## Como funciona

1. O programa de gerenciamento gera uma chave privada RSA de 1024 bits e uma chave publica.
2. A chave publica e salva na raiz do projeto como `public.pem`.
3. A chave privada e salva em `Programa_de_Gerenciamento/private.pem`.
4. O programa de envio cria `Programa_de_Envio/texto.txt` com a mensagem original.
5. Ele calcula o SHA-256 da mensagem em UTF-8 e cifra apenas o hash, salvando-o como `novotexto.txt`.
6. Os dois arquivos sao compactados em `package.zip`.
7. No destino, o ZIP e extraido e o hash cifrado e descriptografado.
8. O hash descriptografado e comparado com o SHA-256 atual de `texto.txt`.

## Estrutura

```text
criptografia-assimetrica/
├── public.pem
├── package.zip
├── Programa_de_Envio/
│   ├── encryptaMensagem.py
│   ├── texto.txt
│   └── novotexto.txt
└── Programa_de_Gerenciamento/
    ├── chaves.py
    ├── private.pem
    └── extracted/
        ├── texto.txt
        └── novotexto.txt
```

Os arquivos `.pem`, `.zip`, `.txt` e o diretorio `extracted/` sao ignorados pelo Git por meio do `.gitignore`.

## Requisitos

- Python 3
- Biblioteca `pycryptodome`

Instale a dependencia:

```bash
pip install pycryptodome
```

## Uso

Execute os programas a partir da raiz do projeto. Os caminhos sao calculados automaticamente em relacao a cada arquivo Python.

### 1. Gerar as chaves

```bash
python Programa_de_Gerenciamento/chaves.py
```

Selecione a opcao `1 - Gerar Chaves`.

O resultado sera:

- `public.pem`: chave publica usada pelo remetente;
- `Programa_de_Gerenciamento/private.pem`: chave privada usada pelo gerenciador.

Mantenha a chave privada em segredo e nao a compartilhe.

### 2. Criar e cifrar a mensagem

```bash
python Programa_de_Envio/encryptaMensagem.py
```

No menu:

1. Escolha `1 - Criar mensagem para enviar` e digite o texto.
2. Escolha `2 - encriptar mensagem` para cifrar o SHA-256 da mensagem.
3. Escolha `3 - Compactar mensagem` para criar `package.zip`.

O ZIP sera criado na raiz do projeto e contera:

- `texto.txt`: texto enviado sem cifragem;
- `novotexto.txt`: hash SHA-256 cifrado com RSA-OAEP.

A operacao de compactacao encerra o programa.

### 3. Descompactar e validar

```bash
python Programa_de_Gerenciamento/chaves.py
```

No menu:

1. Escolha `2 - Descompactar` para extrair `package.zip` em `Programa_de_Gerenciamento/extracted/`.
2. Escolha `3 - Validar arquivo` para descriptografar o hash e comparar com o hash do texto extraido.

O programa exibira uma das respostas:

- `Arquivo Auntêntico`: os dois hashes sao iguais;
- `Arquivo não Autêntico`: os hashes sao diferentes.

A opcao de validacao tambem encerra o programa.

## Observacao de seguranca

Neste projeto, `texto.txt` permanece legivel no ZIP. O RSA-OAEP e usado para cifrar o hash, nao o texto original. Essa implementacao demonstra a verificacao de integridade; para uma troca segura de dados, o texto tambem deveria ser cifrado e o hash deveria ser protegido por uma assinatura digital com a chave privada, em vez de apenas cifrado com a chave publica.