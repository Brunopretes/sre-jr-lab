# Laboratório SRE Junior: Infraestrutura Escalável e Monitorada

Este projeto demonstra a implementação de uma arquitetura completa utilizando práticas de SRE (Site Reliability Engineering), focando em automação, observabilidade e resiliência.

## 🏗️ Arquitetura do Projeto
A solução é composta por 4 camadas principais rodando em Docker:

* **Proxy Reverso:** Nginx (Porta 80) para recebimento de tráfego.
* **API:** FastAPI (Python 3.12) com Health Checks ativos para auto-recuperação.
* **Banco de Dados:** PostgreSQL 16 com volumes persistentes para logs de acesso.
* **Observabilidade:** Netdata para métricas de performance (CPU, RAM, I/O) em tempo real.



## 🛠️ Tecnologias Utilizadas
* **Ansible:** Automação total do provisionamento e deploy (IaC).
* **Docker & Docker Compose:** Containerização e orquestração de serviços.
* **UFW (Uncomplicated Firewall):** Segurança e endurecimento da camada de rede.
* **SQLAlchemy:** ORM para integração e persistência de dados.

## 🚀 Como rodar o projeto

### 1. Pré-requisitos
Ter o Ansible instalado na máquina de controle (Mint) e acesso SSH ao servidor (Ubuntu).

### 2. Configuração do Inventário
Atualize o arquivo `ansible/hosts.ini` com o IP correto do seu servidor:
ini```
[servers]
ubuntu_lab ansible_host=IPServer ansible_user=sre

### 3. Execução do Deploy

Rode o playbook para configurar toda a infraestrutura automaticamente:
Bash

ansible-playbook -i ansible/hosts.ini ansible/deploy.yml

## 📊 Monitoramento e Testes

    Status da API: Acesse http://<IP_DO_SERVIDOR>/status para validar o registro de logs.

    Painel Netdata: Acesse http://<IP_DO_SERVIDOR>:19999 para métricas em tempo real.

## 💾 Operações de SRE (Backup)

```Para realizar o backup do banco de dados diretamente para sua máquina local (Controle):

ssh sre@<IP> "docker exec lab-db-postgres pg_dump -U sre_user lab_db" > backup_projeto.sql