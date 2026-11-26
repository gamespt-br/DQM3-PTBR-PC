# Proteção da branch principal — mantenedor solo

O repositório é mantido por uma única pessoa. Não é necessário convidar alguém sem confiança apenas para cumprir uma exigência de revisão.

## Configuração recomendada para um único mantenedor

Edite **Settings → Rules → Rulesets → proteger-main**.

- Enforcement status: **Active**.
- Target branches: preferencialmente somente **main**.
- Bypass actors: **nenhum**.
- Restrict deletions: **ativado**.
- Block force pushes: **ativado**.
- Require a pull request before merging: **ativado**.
- Required approvals: **0** (zero).
- Require conversation resolution: **ativado**, se disponível.
- Require status checks to pass: **ativado**, selecionando o check **validar-arquivos-publicos**.

Não ative regras que exijam aprovação de outra pessoa, aprovação de Code Owner ou aprovação de alguém diferente do último autor do push, pois não existe outro revisor de confiança no projeto.

## O que essa configuração garante

- Alterações na `main` precisam ser propostas por Pull Request.
- O próprio mantenedor pode abrir e integrar seu Pull Request, sem aprovação externa, desde que as verificações exigidas passem.
- O GitHub Actions executa o validador `validar-arquivos-publicos` nas Pull Requests.
- A branch continua protegida contra exclusão e force push.

## O que ela NÃO garante

- Não é uma revisão independente: o mantenedor continua sendo a única pessoa que avalia e integra as alterações.
- O validador procura extensões proibidas, arquivos grandes e alguns padrões comuns de segredo. Ele não substitui uma auditoria de segurança completa.
- Um Pull Request não garante que o código ou documentação estejam corretos; é uma etapa para inspecionar o diff antes do merge.

## Estado verificado anteriormente

O ruleset `proteger-main` foi encontrado ativo, sem bypass actors, com regras de exclusão e non-fast-forward. A API do GitHub retornou `protected: true` para `main`. A configuração de PR e status check acima é o reforço recomendado para o mantenedor solo.

## Como editar

1. Abra [Settings → Rules → Rulesets](https://github.com/xosonijo-prog/DQM3-PTBR-PC/settings/rules).
2. Abra `proteger-main`.
3. Ajuste o alvo para `main`, caso queira proteger somente a principal.
4. Ative **Require a pull request before merging**.
5. Deixe **Required approvals** em `0`.
6. Ative **Require status checks to pass** e selecione `validar-arquivos-publicos`.
7. Mantenha exclusão e force push bloqueados.
8. Salve e confirme que o ruleset continua **Active**.

Documentação oficial: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets
