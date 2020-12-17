# Aplicação em Python

Esta aplicação em python é um pequeno exemplo utilizando o framework flask.

Será preciso utilizar um banco de dados compatível com MySQL.

## Provisionar

Abaixo temos duas formas de provisionar a aplicação, a primeira é utilizando o virtualenv, a segunda o docker. Independente da forma, será necessário criar o banco:

```bash
docker container run -d --name mariadb -e MYSQL_ROOT_PASSWORD=Abc123_ -e MYSQL_USER=container -e MYSQL_PASSWORD=4linux -e MYSQL_DATABASE=container -v dados:/var/lib/mysql mariadb
```

A aplicação utiliza as seguintes variáveis de ambiente:

- `DB_HOST` - O endereço do banco.
- `DB_NAME` - O nome da base de dados existente no banco.
- `DB_USER` - O nome do usuário que irá se conectar ao banco.
- `DB_PASS` - A senha do usuário citado acima.

> **Observação:** Para os exemplos abaixo, o endereço IP do banco foi considerado como 172.17.0.2.

### Virtualenv

Se possuir python em sua máquina, é possível utilizar o pip diretamente:

```bash
git clone https://github.com/4linux/containers-apps
cd containers-apps/python
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
DB_HOST=172.17.0.2 DB_USER=container DB_PASS=4linux DB_NAME=container flask run
```

### Docker

Caso esteja utilizando Docker será necessário criar um volume. Abaixo um exemplo com alpine:

```bash
git clone https://github.com/4linux/containers-apps
cd containers-apps/python
docker container run -dti --name flask -v $PWD:/opt/app -p 5000:5000 alpine sh
apk add py3-pip
pip3 install -r requirements.txt
DB_HOST=172.17.0.2 DB_USER=container DB_PASS=4linux DB_NAME=container flask run --host 0.0.0.0
```
