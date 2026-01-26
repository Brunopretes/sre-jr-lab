# Laboratório SRE Junior: Infraestrutura Escalável e Monitorada

Este projeto demonstra a implementação de uma arquitetura completa utilizando práticas de SRE (Site Reliability Engineering), focando em automação, observabilidade e resiliência.

## 🏗️ Arquitetura do Projeto
A solução é composta por 4 camadas principais rodando em Docker:
- **Proxy Reverso:** Nginx (Porta 80)
- **API:** FastAPI (Python 3.12) com Health Checks ativos
- **Banco de Dados:** PostgreSQL 16 com volumes persistentes
- **Observabilidade:** Netdata para métricas de performance em tempo real



## 🛠️ Tecnologias Utilizadas
- **Ansible:** Automação do provisionamento e deploy.
- **Docker & Docker Compose:** Containerização e orquestração local.
- **UFW (Uncomplicated Firewall):** Segurança da camada de rede.
- **SQLAlchemy:** Integração e persistência de dados.

## 🚀 Como rodar o projeto
1. **Configuração do Inventário:**
   Atualize o arquivo `ansible/hosts.ini` com o IP do seu servidor.
   
2. **Execução do Deploy:**
   ```bash
   ansible-playbook -i ansible/hosts.ini ansible/deploy.yml

3. **Execução do Deploy**

Rode o playbook para configurar toda a infraestrutura automaticamente:
Bash

ansible-playbook -i ansible/hosts.ini ansible/deploy.yml