# tutorial_doker

## Instalação

Sequir as orientações da documentação clicando [aqui!](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)
Dica: Usar o script que está na documentação clicando [aqui!](https://docs.docker.com/engine/install/ubuntu/#install-using-the-convenience-script)

### Lista de comandos:

#### Lista geral
`docker --help`

#### Lista por comando específico (Exemplificado com o comando *run*)

`docker run --help`
### baixar imagem

Exemplificando com imagem ubuntu:

`docker pull ubuntu`

### Listar imagens baixadas

`doker images`

### Executrando containers

#### modo simples:
`docker run ubuntu`

#### Por tempo determinado (por 10 segundos)
`docker run ubuntu sleep 10` 

OBS: Esta opção trava o console. Para destravar, acesse de outro terminal e use o comando `docker stop NAME/CONTAINER ID` informando o nome ou o id do container

#### Com terminal interativo
`docker run -it ubuntu`

Onde: 
-i = interativo
-t = pseudo-terminal

Obs: Esta opção encerra o container ao sair.

#### Com terminal interativo
`docker run -dit ubuntu`

Onde:
-d = Background (só será encerrado com o comando stop)

Ao final deste comando aparecerá na tela o CONTAINER ID completo. Use este número para acessar este container.

para acessá-lo depois:

`docker exec -it CONTAINER ID /bin/bash`
Onde:
CONTAINER ID = número do id do container (pode ser só os primeiros números)
/bin/bash = indicando que é para executar o bash (terminal)



### Visualizar containers em execução

#### Ativos no momento:
`docker ps`

#### Histórico:
`docker ps -a`

### Remover container:
`rocker rm CONTAINER ID`

### Remover imagens:

`docker rmi ubuntu`

### Criando container com nomes

OBS: Caso não tenha estas imagens no PC elas serão baixadas automaticamente

`docker run -dti --name ubuntu_01 ubuntu`

`docker run -dti --name debian_01 debian` 

`docker run -dti --name alpine_01 alpine` 

### Manipulando container usando exec sem ter que logar

#### Criando uma pasta

`docker exec ubuntu_01 mkdir /destino`

#### Enviando um arquivo

`docker cp local_e_nome_do_arquivo ubuntu_01:/destino`

#### verificando se a transferência foi feita

`docker exec ubuntu_01 ls /destino -lh`

#### pegando um arquivo

`docker cp ubuntu_0:/destino/nome_do_arquivo salvar_como_local_e_nome_do_arquivo`

### Uso ds Tag's para baixar verções específicas

Obs: Verifique em **dockerhub** as tag's disponíveis. No exemplo abaixo é baixada a imagem da versão 9 do debian
`docker pull debian:9`

#### Usando a imagem baixada:

`docker run -dti debian:9`

### Exemplo MySQL

#### Baixando imagem

`docker pull mysql`

#### Criando o container

~~~shell
docker rum -e MYSQL_ROOT_PASSWORD=Senha123 --name mysql-A -d -p 3306:3306 mysql
# -e = configura variáveis de ambiente (MYSQL_ROOT_PASSWORD)
# --name = nomeia o container
# -d = deixa rodando em backgroud
# -p = configura a porta
# ao final informar a imagem usada (mysql)
~~~

#### Acessando o container para configurá-lo

##### Acessando o container

`docker exec -it mysql-A bash`

##### Acessando o mysql como root

`mysql -u root -p --protocol=tcp`

#### Criando database


`CREATE DATABASE TESTE;`

Saia do **MySQK** e do **container** caso não tenha mais nada que queira configurar desta forma

#### Verificando informações do container

Obseve a faixa de *IP*

`docker inspect mysql-A`

#### Conectando ao *MySQL* diretamente do pc host

Caso o IP *27.0.0.1* esteja configurado, o código abaixo irá funcionar

`mysql -u root -p --protocol=tcp`

#### Conectando ao *MySQL* através de uma máquina externa

Use um **SGBD** de sua preferência para acessar o banco, lembrando que o IP informado deve ser o da máquina host do *docker*

--16
