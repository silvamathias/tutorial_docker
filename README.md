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
# -p = configura a porta sendo: host:container
# ao final informar a imagem usada (mysql)
~~~

Note quê, ao declarar a porta, primeiro informe a porta do host (servidor/máquina onde o docker está instalado) e depois informe a porta do container.

#### Acessando o container para configurá-lo

##### Acessando o container

`docker exec -it mysql-A bash`

##### Acessando o mysql como root

`mysql -u root -p --protocol=tcp`

#### Criando database


`CREATE DATABASE TESTE;`

Saia do **MySQL** e do **container** caso não tenha mais nada que queira configurar desta forma

#### Verificando informações do container

Obseve a faixa de *IP*

`docker inspect mysql-A`

#### Conectando ao *MySQL* diretamente do pc host

Caso o IP *27.0.0.1* esteja configurado, o código abaixo irá funcionar

`mysql -u root -p --protocol=tcp`

#### Conectando ao *MySQL* através de uma máquina externa

Use um **SGBD** de sua preferência para acessar o banco, lembrando que o IP informado deve ser o da máquina host do *docker*

### interromper um container

#### Parar um container

`docker stop nome_do_container`

#### iniciando um container que foi pauado

`docker start nome_do_container`

#### Removendo um container

**OBS:** Só pode remover um container que esteja pausado

`docker rm nome_do_container`

### Inspecionando um container

`docker inspect nome_do_container`

### Redirecionando volume de dados para uma pasta no PC host

#### Volume tipo Bind
esta ação deixa os dados do container salvos em uma pasta do PC, preservando os dados mesmo que o container seja deletado

use as tag:

`--volume=/pasta/do/pc/host:/pasta/dentro/do/container`

O comando acima *--voluma* usa o método **Bind** para montar uma pasta do host dentro do container

Pode criar uma pasta no host antecipadamente para guardar os dados e informá-la no comando acima

uma opção é usar o comando:

`--mount type=bind, src=/pasta/do/pc/host, dst=/pasta/dentro/do/container,ro`

O comando `ro` é opcional caso queira que seja somente leitura
 
#### Volume tipo naimed

listar volumes

`docker volume ls`

os volumes ficam na pasta padrão do docker em */var/lib/docker/volumes*

Os arquivos ficam dentro de cada volume na pasta *_data*

crie um volume com o comando abaixo

`docker volume create nome_do_volume`

ao crfiar um container informe o nome do volume criadoao invés da pasta no host

`--mount type=volume, src=nome_do_volume,dst=/data`

para excluir o volume, use:

`docker volume rm nome_do_volume`

Excluindo todos os volumes sem uso

`docker volume prune`

O comando *prune* também pode ser usado para deletar todos os container's

`docker container prune`

Para remover um container de forma forçada em ter que pará-lo primeiro

`docker rm -f nome_do_container`

### Redes

#### Listar redes

`docker network ls`

#### Criar uma rede

`docker network create nome_da_rede`

#### Usar a rede criada

`... --network nome_da_rede`

OBS: É possível usar o comando `inspect` para ver os detalhes da rede da menma forma com outros objetos

### Criando imagens

Criar imagens permite salvarcustomizar uma imagem já existente definindo valores de variáveis de ambiente, configuraçã ode arquivos, instalação de programas, etc.

Para criar a imagem devesse criar um arquivo de nome **dockerfile** com os comandos para configurar a nova imagem. Abaixo lista dos comandos usados.

**Comando**|**Descrição**
|:---:|:---|
ADD|Baixa da internet ou copia do próprio PC pastas ou arquivos para dentro da imagem.
ARG|Usa variações para o comando build-time.
CMD|Determina o comando que a imagem irá rodar.
COPY|Copia apenas do PC pastas ou arquivos para dentro da imagem.
ENTRYPOINT|Especifica executor padrão
ENV|Configura variaveis de ambiente.
EXPOSE|Informar a porta que o aplicativo está escutando
FROM|Informa uma imagem que será usada como base.
HEALTHCHECK|Verifica ao iniciar se o container está íntegro.
LABEL|Adiciona metadados a uma imagem.
MAINTAINER|Especifique o autor da imagem.
ONBUILD|Especifique instruções para quando a imagem for usada em uma build.
RUN|Executa os comandos da build.
SHELL|Defina o shell padrão da imagem.
STOPSIGNAL|Configura o sinal de chamada do sistema para sair de um contêiner.
USER|Defina o ID do usuário e do grupo.
VOLUME|Cria montagens de volume.
WORKDIR|Altera diretório de trabalho.

#### Exemplo de distro linux com script python

Na pasta **dockerfile_gfx** está um projeto para criar uma imagem utilizando a distribuição linux *ubuntu* como base e instalando nele o *python*, depois instala as bibliotecas necessárias, importa para a imagem o script python *app.py* e configura este script como programa padrão ao executar o container

Abaixo segue transcrição do arquivo *dockerfile* do projeto. 

~~~shell
FROM ubuntu
RUN apt-get update 
RUN apt-get install -y python3 
RUN apt-get clean
RUN apt-get install -y python3-matplotlib
RUN apt-get install -y python3-numpy
COPY app.py /opt/app.py
CMD python3 /opt/app.py
~~~

Abaixo segue transcrição do script python contido no arquivo *app.py*.

~~~python
import numpy as np
import matplotlib.pyplot as mp 


# %%
a = np.linspace(0,4*np.pi,400)

# %%
y1 = np.sin(a)

# %%
y2 = np.cos(a)

# %%
mp.plot(a,y1)
mp.plot(a,y2)
mp.show()

# %%
fig, gx = mp.subplots(2,1)
gx[0].plot(a,y1)
gx[1].plot(a,y2)
mp.show()

print(a)
~~~

OBS: O arquivo que será importado paa dentro da imagem deve estar na mesma pasta que o arquivo *dockerfile*.

Este script foi feito com o objetivo de plotar gráficos da curva seno e cosseno. Ele irá funcionar caso rode no python mas não aparecerá o gráfico caso rode a imagem criada com ele. Como o objetivo é testar do docker eu mantive este exemplo mas coloquei o comando *print* ao final para que ele imprima uma das listas de números usadas para criar os gráficos. Desta forma o arquivo *dockerfile* foi mantido com bons exemplos de como usar uma distro, atualizar a distro, instalar um programa (python3), instalar uma biblioteca do programa (numpy e matplotlib), copiar um arquivo para dentro da imagem (app.py) e configurar a programação padrão da imagem.

Com os arquivos *dockerfile* e *app.py* criados, basta rodar o comando abaixo de dentro da pasta onde os mesmos estão salvos.

~~~shell
docker build -t pyfx .
~~~

O comando `docker build` cria a imagem, a opção `-t` permite informar o nome da imagem e a tag, neste exemplo o nome é *pyfx*, e ao final temos o sinal e ponto `.` para informar que o arquivo *dockerfile* está na pasta atual.

#### Exemplo de distro linux com programa instalado (neofetch)

Na pasta **dockerfile_neofetch** está um projeto para criar uma imagem utilizando a distribuição linux *ubuntu*, atualizar a distro, instalar um pacote (neofetch) e configurá-lo como comando padrão ao executar o container.

Abaixo segue transcrição do arquivo *dockerfile* do projeto.

~~~shell
FROM ubuntu
RUN apt-get update && apt-get install -y neofetch
RUN apt-get clean
CMD neofetch
~~~

Com os arquivos *dockerfile* criado, basta rodar o comando abaixo de dentro da pasta onde o mesmo está salvo.

~~~shell
docker build -t ubuntu_nft .
~~~

O comando é o mesmo do exemplo anterior, apenas foi informado outro nome para a imagem (ubuntu_nft).
