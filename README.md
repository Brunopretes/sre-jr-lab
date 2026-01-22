# Laboratório SRE Junior - API Conteinerizada

Este projeto demonstra uma arquitetura básica de SRE, automatizando a infraestrutura e o deploy de uma API FastAPI.

## 🏗️ Arquitetura
- **Host Local:** Linux Mint (Estação de Controle)
- **Servidor:** Ubuntu Server (Host de Aplicação)
- **Proxy Reverso:** Nginx (Porta 80)
- **Backend:** FastAPI (Python 3.12)
- **Automação:** Ansible

## 🛠️ Tecnologias Utilizadas
- **Docker & Docker Compose:** Conteinerização e orquestração local.
- **Ansible:** Configuração de servidor e entrega contínua (CD).
- **GitHub:** Versionamento de código.

## 🚀 Como rodar o deploy
1. Certifique-se de que o SSH entre o Host e o Server está configurado.
2. Prepare o servidor:
   `ansible-playbook -i ansible/hosts.ini ansible/setup.yml --ask-become-pass`
3. Realize o deploy:
   `ansible-playbook -i ansible/hosts.ini ansible/deploy.yml`

## 📊 Monitoramento
Para visualizar o consumo de recursos:
`ssh user@ip-do-servidor "docker stats"`