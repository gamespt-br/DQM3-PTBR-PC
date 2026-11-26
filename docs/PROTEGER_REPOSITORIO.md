# Configurar proteção da branch principal

A integração conectada permite publicar e revisar arquivos do repositório, mas não disponibiliza aqui a operação administrativa de criação de regras de branch. A configuração abaixo precisa ser feita pelo proprietário na interface do GitHub.

## Criar um ruleset para main

1. Abra **Settings → Rules → Rulesets** no repositório.
2. Clique em **New branch ruleset**.
3. Nome: `proteger-main`.
4. Em enforcement status, selecione **Active**.
5. Em target branches, selecione a branch padrão `main`.
6. Não conceda bypass a terceiros. Se houver uma opção para bypass de administradores, considere cuidadosamente se deseja mantê-la; para maior proteção, não conceda bypass desnecessário.
7. Ative:
   - **Restrict deletions**.
   - **Block force pushes**.
   - **Require a pull request before merging**.
   - **Require linear history**, após habilitar squash ou rebase merge nas configurações de Pull Requests, se necessário.
8. Para evitar bloquear o mantenedor que trabalha sozinho, deixe o número de aprovações obrigatórias em zero inicialmente. Não habilite “Require review from Code Owners” até existir outro revisor que possa aprovar os PRs.
9. Salve em **Create ruleset**.

## Verificação

Depois de salvar, a página Rulesets deve mostrar `proteger-main` com status Active e alvo `main`.

A documentação do GitHub informa que rulesets estão disponíveis em repositórios públicos no plano Free e que administradores do repositório podem criá-los:
https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository

## Segurança complementar

- Ative autenticação em dois fatores na conta GitHub.
- Em Settings → Code security and analysis, habilite os recursos de secret scanning disponíveis para o repositório.
- Não adicione tokens, senhas, saves ou arquivos originais/modificados do jogo.
- O workflow `.github/workflows/validar-conteudo-publico.yml` verifica extensões proibidas, tamanho e alguns padrões comuns de segredos em PRs e commits na `main`. Ele é uma defesa complementar, não substitui revisão.
