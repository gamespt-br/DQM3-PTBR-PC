# Estado da proteção do repositório

O repositório possui atualmente um ruleset ativo chamado `proteger-main`.

- **Status:** Active.
- **Alvo configurado:** todas as branches (`~ALL`), não apenas `main`.
- **Restrict deletions:** ativo.
- **Block force pushes:** ativo (regra `non_fast_forward`).
- **Bypass actors:** nenhum.
- **Require a pull request before merging:** não está ativado no ruleset atual.
- **Aprovações obrigatórias:** não configuradas.

A API do GitHub também retorna `protected: true` para a branch `main`.

## Avaliação

A configuração atual impede exclusões de branches e atualizações não fast-forward. Ela não obriga o uso de Pull Requests: como não há exigência de PR, alterações normais podem continuar sendo enviadas diretamente às branches por pessoas com permissão de escrita.

Se desejar exigir revisão antes de qualquer alteração na `main`, edite o ruleset em **Settings → Rules → Rulesets → proteger-main** e acrescente a regra **Require a pull request before merging**. Para um projeto mantido por uma única pessoa, mantenha o número de aprovações obrigatórias em zero até haver outro revisor.

O ruleset foi configurado para todas as branches. Isso é mais abrangente do que proteger somente `main`; se preferir restringi-lo à branch principal, altere o alvo de branches para incluir somente `main`.

## Segurança complementar

- Mantenha a autenticação em dois fatores habilitada na conta.
- O uso do endereço `users.noreply.github.com` nos commits recentes ajuda a evitar a exposição do e-mail pessoal em novas alterações. Commits anteriores continuam contendo o e-mail utilizado na época.
- O workflow `.github/workflows/validar-conteudo-publico.yml` verifica extensões proibidas, tamanho e alguns padrões comuns de segredos. É uma defesa complementar, não substitui revisão manual nem uma ferramenta abrangente de secret scanning.
- Não adicione tokens, senhas, saves ou arquivos originais/modificados do jogo.

## Links

- [Ruleset proteger-main](https://github.com/xosonijo-prog/DQM3-PTBR-PC/rules/28177619)
- [Configurações de regras](https://github.com/xosonijo-prog/DQM3-PTBR-PC/settings/rules)
- [Documentação oficial do GitHub sobre rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository)
