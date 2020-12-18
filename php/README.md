# Aplicação em PHP

Esta aplicação em PHP é um pequeno exemplo utilizando o framework slim.

Será preciso utilizar um banco de dados PostgreSQL.

## Provisionar

Antes de criar o contêiner, para provisionar a aplicação será necessário criar o banco:

```bash
docker container run -d --name postgres -e POSTGRES_USER=container -e POSTGRES_PASSWORD=4linux -e POSTGRES_DB=container -v dados:/var/lib/postgres postgres:alpine
```

A aplicação utiliza as seguintes variáveis de ambiente:

- `DB_HOST` - O endereço do banco.
- `DB_NAME` - O nome da base de dados existente no banco.
- `DB_USER` - O nome do usuário que irá se conectar ao banco.
- `DB_PASS` - A senha do usuário citado acima.

Uma vez iniciada, a aplicação cadastrará alguns usuários no banco e fornecerá uma simples página para realizar login, utilize um dos seguintes usuários:

- paramahansa@yogananda.in - 123
- victor@frankenstein.co.uk - 123

> **Observação:** Para os exemplos abaixo, o endereço IP do banco foi considerado como 172.17.0.2.

### Docker

```bash
git clone https://github.com/4linux/containers-apps
cd containers-apps/php
docker container run -dti --name slim -v $PWD:/opt/app -p 8080:8080 alpine sh

apk add php-pdo php7-pdo_pgsql composer
cd /opt/app
composer install
DB_HOST=172.17.0.2 DB_USER=container DB_PASS=4linux DB_NAME=container php -S 0.0.0.0:8080
```
