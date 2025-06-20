# Meu Controle de Pressão

[](https://www.python.org/)
[](https://flask.palletsprojects.com/)
[](https://opensource.org/licenses/MIT)

"Meu Controle de Pressão" é uma aplicação web desenvolvida com Flask que permite aos usuários monitorar e registrar suas medições de pressão arterial.

## 📋 Visão Geral do Projeto

Este sistema oferece um conjunto robusto de funcionalidades para o monitoramento de pressão arterial:

  * **Autenticação Completa**: Inclui funcionalidades de cadastro, login e logout de usuários.
  * **Dashboard Personalizado**: Um painel intuitivo para visualização dos dados do usuário.
  * **Registro de Medições**: Permite registrar medições com campos adicionais como horário e remédios tomados.
  * **Classificação Automática**: As medições são classificadas automaticamente para fácil interpretação.
  * **Gráficos Interativos**: Visualize suas tendências de pressão ao longo do tempo.
  * **Filtro por Período**: Permite filtrar as medições por datas específicas.
  * **Exportação de Dados**: Exporte seus dados em formatos PDF e CSV.
  * **Perfil do Usuário**: Área dedicada com foto e dados pessoais.

## 📂 Estrutura de Diretórios

A estrutura organizada do projeto facilita a navegação e a manutenção:

```
meu-controle-pressao-v2/
├── app/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   │   └── main.js
│   │   └── profile_pics/ (Diretório para fotos de perfil)
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── dashboard.html
│   │   └── profile.html
│   ├── instance/
│   │   └── database.db (Banco de dados SQLite)
│   ├── __init__.py
│   ├── models.py
│   ├── forms.py
│   ├── auth_routes.py
│   └── main_routes.py
├── venv/ (Ambiente virtual Python - será criado)
├── requirements.txt
├── run.py
└── .env
```

## 🛠️ Instalação e Configuração

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local:

### 1\. Pré-requisitos

Certifique-se de ter o **Python 3** e o `pip` (gerenciador de pacotes do Python) instalados em seu sistema.

### 2\. Clonar o Repositório ou Descompactar

Se você recebeu o projeto como um arquivo compactado, descompacte-o. Caso contrário, você pode criar a estrutura de diretórios e os arquivos manualmente.

### 3\. Configurar o Ambiente Virtual

É altamente recomendável usar um ambiente virtual para isolar as dependências do projeto.

```bash
# Navegue até o diretório raiz do projeto
cd meu-controle-pressao-v2

# Crie o ambiente virtual
python3 -m venv venv

# Ative o ambiente virtual
# No Linux/macOS:
source venv/bin/activate
# No Windows:
# venv\Scripts\activate
```

### 4\. Instalar Dependências

Com o ambiente virtual ativado, instale as dependências listadas no `requirements.txt`, além de `Pillow` que é necessária para manipulação de imagens de perfil.

```bash
pip install -r requirements.txt
pip install Pillow
```

As dependências principais incluem:

  * `Flask`
  * `Flask-SQLAlchemy`
  * `Flask-Login`
  * `Flask-WTF`
  * `python-dotenv`
  * `Flask-Bcrypt`
  * `email_validator`
  * `Pillow` (PIL)

### 5\. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto (`meu-controle-pressao-v2/`) com o seguinte conteúdo:

```
SECRET_KEY=sua_chave_secreta_aqui
```

Substitua `sua_chave_secreta_aqui` por uma string aleatória e segura. Você pode gerar uma usando Python:

```python
import secrets
print(secrets.token_hex(16))
```

### 6\. Inicializar o Banco de Dados e Diretórios Essenciais

O banco de dados SQLite (`database.db`) será criado automaticamente na primeira vez que a aplicação for executada. Certifique-se de que os diretórios necessários existam:

```bash
# Crie o diretório 'instance' dentro de 'app/'
mkdir -p app/instance

# Crie o diretório 'profile_pics' dentro de 'app/static/' para as fotos de perfil
mkdir -p app/static/profile_pics
```

### 7\. Executar a Aplicação

Com o ambiente virtual ativado, execute o arquivo `run.py`:

```bash
python3 run.py
```

A aplicação estará acessível em `http://localhost:5000` no seu navegador.

## 🚀 Como Usar

1.  **Acesse a Aplicação**: Abra seu navegador e vá para `http://localhost:5000`.
2.  **Cadastro/Login**: Se for seu primeiro acesso, cadastre-se. Caso contrário, faça login com suas credenciais.
3.  **Dashboard**: No dashboard, você poderá adicionar novas medições de pressão arterial, visualizá-las em uma tabela, e acompanhar as tendências em um gráfico.
4.  **Filtros**: Use os campos de data para filtrar suas medições por período.
5.  **Exportação**: Exporte seus dados de medição para CSV ou PDF.
6.  **Perfil**: Atualize seus dados pessoais e foto de perfil na área de perfil.

## 🤝 Contribuição

Contribuições são bem-vindas\! Se você tiver sugestões, melhorias ou encontrar bugs, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## 📄 Licença

Este projeto está licenciado sob a Licença MIT.

