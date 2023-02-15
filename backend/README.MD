# BACKEND FASTAPI
Backend desenvolvido para o desafio técnico IATECAM.

## Features
- Crud básico com FASTAPI;
- Cadastro de produtos;
- Listagem de produtos;
- Atualização de produtos;
- Exclusão de produtos.
- Cadastro de categorias;
- Listagem de categorias;
- Atualização de categorias;
- Exclusão de categorias.

## Tecnologias utilizadas
Para executar o projeto, será necessário instalar/usar os seguintes programas:
* [Python 3.11.2](https://www.python.org/downloads/)
* [MariaDb 10.11.1 RC](https://mariadb.org/)
* [FastApi 0.91.0](https://fastapi.tiangolo.com/)
* [Visual Studio Code](https://code.visualstudio.com/download)

## Instalação 
Para executar esse repositório baixe-o e siga os passos abaixos:
1. Baixe e instale o python na versão 3.11.2
2. Baixe e instale o banco de dados MariaDb na versão 10.11.1 RC <br>
    2.1. A conexão do banco de dados no backend está configurado para acessar pelo usuário: root e senha: 123, configure dessa forma, quando pedir senha e usurio do root.
    Caso seja necessário mudar. altere os arquivos backend\sql_app\core\database.py e backend\sql_app\automat_db\create_db.py , com os usuários senha definidos
3. Baixe o reposítorio ou realize um git clone.
4. Abra o visual Visual Studio Code e navegar até a pasta \backend\sql_app atráves do comando cd
5. Na pasta anterior indicada, para instalar as outras dependências do backend execute o arquivo: requirements.txt, da seguinte forma: pip install -r requirements.txt

## Execução do BackEnd
Para executar o backend entre nas pastas(backend/sql_app) e execute o seguinte comando: uvicorn main:app --reload 
