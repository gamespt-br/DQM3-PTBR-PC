# Instalação — Atualização 13 (PC)

## Pacote de referência

A instalação local de teste foi preparada com base no pacote fornecido pelo mantenedor:

- Pacote-fonte: `DQM3_PTBR_Auditoria_PC_Atualizacao_13_DLCs.zip`
- Atualização: **13**, cumulativa sobre `DQM3_PTBR_Auditoria_PC_Atualizacao_12.zip`
- Bundle interno: `3e214ed0d6baa09fe6b312ba2b7a80d119e8a20b65753aa5a933a745e04050c4`
- SHA-256 do bundle: `1fe24d881b8afb70b549c338f3b09d3ee1b2768e2590e22ba279b7c9eb5dd17f`
- Destino: `DQMonsters3_Data\StreamingAssets\AB\` (substitui o bundle com o mesmo nome).

## Instalador local de teste

O pacote privado de teste preparado para o mantenedor inclui os scripts `Instalar_PTBR.ps1` e `Restaurar_PTBR.ps1`. Esses arquivos não estão incluídos no repositório público porque o pacote local contém o bundle completo do jogo.

O instalador:

1. Confere o SHA-256 do bundle incluído no pacote.
2. Solicita a pasta principal do jogo, que deve conter `DQMonsters3.exe` e `DQMonsters3_Data`.
3. Confirma que o diretório `StreamingAssets\AB` e o bundle esperado existem.
4. Interrompe a instalação se o jogo estiver em execução.
5. Faz backup do bundle atualmente instalado em `Documents\DQM3_PTBR_Backups`.
6. Copia o bundle PT-BR e verifica novamente o SHA-256.
7. Registra um manifesto para permitir restauração.

O script de restauração verifica o backup e o hash do bundle atual. Se o arquivo tiver sido alterado depois da instalação (por exemplo, por uma atualização oficial do jogo), a restauração automática é interrompida para evitar sobrescrever dados mais recentes.

## Procedimento de teste local

1. Feche o jogo.
2. Extraia o pacote local de instalador.
3. Execute `Instalar_PTBR.ps1` pelo PowerShell. Se necessário, abra o PowerShell nessa pasta e execute:
   `powershell -NoProfile -ExecutionPolicy Bypass -File .\Instalar_PTBR.ps1`
4. Selecione a pasta que contém `DQMonsters3.exe` e `DQMonsters3_Data`.
5. Mantenha o idioma do jogo em **Espanhol**, conforme o LEIA-ME da Atualização 13.
6. Abra o jogo e teste a inicialização, menus, diálogos e os rótulos/conteúdos das três DLCs.
7. Para voltar ao arquivo anterior, execute `Restaurar_PTBR.ps1` e selecione o manifesto criado em `Documents\DQM3_PTBR_Backups`.

## Escopo da Atualização 13

- 22 células alteradas em 5 TextAssets.
- `The Mole Hole`: rótulo curto `Toca` (limite de seis bytes); a forma completa `Toca da Toupeira` permanece nas telas de ajuda e no nome de acesso.
- `Coach Joe's Dungeon Gym`: referências residuais alinhadas para `Ginásio do Mestre Camarão`.
- `Treasure Trunks`: `Baú do Tesouro` / `Baús do Tesouro`, com gênero gramatical corrigido.
- Textos de ajuda comuns e variantes Windows/PC revisados.
- Variantes específicas de Nintendo Switch (NX) e celular (SP) mantidas intactas.
- Os 533 nomes originais dos monstros permanecem byte a byte idênticos.

## Estado da validação

O relatório incluído no pacote-fonte registra aprovação das verificações estruturais, integridade ZIP, reconstrução UnityFS, ida/volta AES, preservação dos tamanhos e alteração apenas dos intervalos esperados. O mesmo relatório marca o teste final dentro do jogo como **pendente de confirmação do usuário**. Portanto, o instalador local é um pacote de teste até essa confirmação.

## Distribuição pública — bundle não incluído

O pacote local de teste contém o bundle completo do jogo. Ele não deve ser enviado ao repositório, incluído em uma Release pública ou distribuído pela Steam sem revisão de direitos e permissões.

A preparação de um formato público que não redistribua dados originais do jogo desnecessariamente permanece pendente de revisão técnica e de permissões. Esta documentação não concede licença para distribuir conteúdo da Square Enix.

## Avisos

- A compatibilidade confirmada em uma instalação não garante compatibilidade com todos os PCs ou futuras atualizações oficiais.
- Não use o pacote em versões/builds diferentes sem validação.
- Não mantenha o jogo aberto durante a instalação ou restauração.
