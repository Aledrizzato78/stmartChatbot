# 🤖 Chatbot Portfólio - Projeto em Python + Django com AWS (EC2 + S3)

Este projeto é um chatbot inteligente integrado ao meu portfólio online. Desenvolvido com Django, hospedado em uma instância EC2 da AWS, e conectado com um front-end estático hospedado no S3. Ideal para mostrar criatividade, domínio de infraestrutura e integração moderna com APIs externas.

---

## 🌐 Demonstração
👉 [Acesse aqui o portfólio com o chatbot](https://alexdrizzato.s3-website-sa-east-1.amazonaws.com)

---

## 🧰 Tecnologias Utilizadas

- Python 3.10  
- Django 5.x  
- HTML5 + CSS3 + JavaScript (Vanilla)  
- AWS EC2 (Ubuntu 22.04)  
- AWS S3 (site estático público)  
- AWS CLI  
- Shell Script (para automação do `env.js`)

---

## 💬 Funcionalidades do Chatbot

- 👋 Saudações personalizadas (`oi`, `bom dia`, `boa tarde`, etc.)
- 🩺 Respostas de mock API (`status`, `ping`, `health`, `versao`)
- ☀️ Clima em tempo real (Open-Meteo)
- 💵 Cotação do dólar (AwesomeAPI)
- 🕒 Hora e data atual
- 🤖 Avatar 64bits amigável estilo assistente virtual
- 📱 Integração com WhatsApp via botão flutuante

---

## ⚙️ Execução do Projeto

### ✅ Requisitos:
- AWS CLI configurado com access key
- Instância EC2 configurada e acessível via `.pem`
- Bucket S3 com `index.html`, `env.js`, e `avatar-bot.png` públicos

### 📦 Clonar repositório:

```bash
git clone https://github.com/Aledrizzato78/chatbot-portfolio.git
cd chatbot-portfolio
```

### 🐍 Criar ambiente virtual e instalar dependências:

```bash
python3 -m venv venv
source venv/bin/activate
pip install django requests
```

### 🚀 Iniciar o servidor:

```bash
python manage.py runserver 0.0.0.0:8000
```

---

## 🔁 Automatização com Bash

O script `atualiza-env.sh` faz:

- Obtenção do IP público da EC2
- Geração do `env.js` com o IP atualizado
- Upload automático para o S3 com permissão pública

### 🔧 Executar:

```bash
cd ~/.ssh
./atualiza-env.sh
```

---

## 📁 Estrutura do Projeto

```
chatbot-portfolio/
├── chat/
│   └── views.py
├── core/
│   └── settings.py
├── env.js       ← gerado via script
├── index.html   ← hospedado no S3
├── avatar-bot.png
└── atualiza-env.sh
```

---

## 📸 Tela do Projeto

> Insira aqui uma imagem do site com o bot flutuante aparecendo (ex: `screenshot.png`)

---

## 👨‍💻 Autor

**Alexandre Drummond Rizzato**  
[GitHub](https://github.com/Aledrizzato78) | [LinkedIn](https://www.linkedin.com/in/alexandre-drummond-rizzato-524a3724)

---

## 📄 Licença

Este projeto está sob a licença MIT.
