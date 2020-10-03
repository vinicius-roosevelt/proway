<!-- 
    ** README of the project **
    This file contains the instructions and information for runnning and using the system locally
    Created by: Vinicius Roosevelt Santos Dias
 -->

<p align="center" style="width: 500px;">
    <img src="https://www.flaticon.com/svg/static/icons/svg/1822/1822899.svg"><br/>
    Projeto do desafio prático - Pública Tecnologia
</p>

<!-- ABOUT THE PROJECT -->
## Sobre o projeto

Este repositório contém o sistema solicitado no desafio prático pela empresa de tecnlogia Pública.

O projeto desenvolvido tem como objetivo apresentar as qualificações do candidato, como também, aprimorar os conhecimentos
e habilidades em programação.

Este sistema contém:
* Interface para consulta de dados e apresentação de gráficos e informações de maneira intuitiva
* Interface para incerção de novos dados no sistema
* Cálculo automatizado de pontuação mínima da temporada, pontuação máxima da temporada, e quantidade de vezes que os recordes foram quebrados

### Criado com:
Este sistema foi desenvolvido em python, com auxílio do framework Django, para trabalhar com os dados enviados e solicitados do banco de dados<br>
Além disso, também foram utilizados no sistema:
* Jquery
* DataTable jquery plugin
* Jquery UI

<!-- GETTING STARTED -->
## Utilizando o sistema

Como o projeto foi desenvolvido em python, alguns procedimentos devem ser realizados para permitir o funcionamento.<br/>
Em python, quando um projeto é desenvolvido, um ambiente virtual é criado para separar o projeto do computador. Dessa forma
é possível tornar o sistema menos dependente de bibliotecas e pacotes instalados no computador do desenvolvedor.

No caso do Python, o ambiente virtual precisa ser inicializado para poder instalar os pacotes python e rodar o sistema.

### Pré requisitos

* Python (com gerenciador de pacotes pip)

### Preparação do sistema

Considerando que o python já está instalado em sua máquina, devemos baixar o código fonte, inicializar o sistema e, então, tudo estará pronto para uso.

Os passos para reprodução são:

#### 1. Clonar este repositório
Caso tenha o git instalado no computador, isso pode ser feito com o comando abaixo:
```
git clone https://github.com/vinicius-roosevelt/proway.git
```
Caso o git nao esteja instalado, voce pode fazer o download do código [aqui](https://github.com/vinicius-roosevelt/proway) e extrair a pasta compactada no diretório que desejar.

#### 2. Inicializando o ambiente virtual:
Para inicializar o ambiente virtual, e assim, instalar os pacotes e rodar o servidor, vá até a pasta '/env/Scripts' com o propt de comando do windows<br>
com o prompt de comando no diretório especificado, deve-se executar o seguinte comando:

```
activate.bat
```

Quando o ambiente virtual estiver inicializado, irá aparecer "(env)" no início das linhas de comando.

#### 3. Instale as dependencias no ambiente virtual
Para instalar os pacotes e dependencias, volte até o diretório '/env' no prompt de comando e digite o comando

```
pip install -r requirements.txt
```

Com isso o python irá instalar, automaticamente, todos os pacotes que foram utilizados no sistema.

#### 4. Inicie o servidor web

Depois de seguir os passos, nosso ambiente virtual está preparado e configurado para rodar o sistema. Agora, é preciso ir na pasta '/system/', ainda no prompt de comando, e rodar o seguinte comando:

```
python manage.py runserver 
```

Após isso, o prompt irá apresentar algo como:
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 03, 2020 - 16:49:56
Django version 3.1.1, using settings 'project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

Isso significa que o sistema está rodando normalmente. Para utiliza-lo, basta acessar o link 'http://127.0.0.1:8000' em seu navegador

### Fornecendo dados iniciais ao sistema.
Caso queria inicializar os sitema com algums dados, antes de rodar  o comando ``` python manage.py runserver```, execute o seguinte comando:
```
    python manage.py loaddata project/fixtures/data.json
```

Esse comando irá buscar pelo arquivo 'data.json' e inserir os objetos encontrados nesse arquivo no sistema.

## Usando o sistema

Como mencionado acima, quando o servidor estiver rodando normalmente, basta acessar o link 'http://127.0.0.1:8000' em seu navegador.
