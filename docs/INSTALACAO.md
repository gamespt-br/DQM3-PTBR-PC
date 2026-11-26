# Instalação — Atualização 13 (PC)

## Pacote de referência

A instalação local de teste foi preparada com base no pacote fornecido pelo mantenedor:

- Pacote-fonte: `DQM3_PTBR_Auditoria_PC_Atualizacao_13_DLCs.zip`
- Atualização: **13**, cumulativa sobre `DQM3_PTBR_Auditoria_PC_Atualizacao_12.zip`
- Bundle interno: `3e214ed0d6baa09fe6b312ba2b7a80d119e8a20b65753aa5a933a745e04050c4`
- SHA-256 do bundle: `1fe24d881b8afb70b549c338f3b09d3ee1b2768e2590e22ba279b7c9eb5dd17f`
- Destino: `DQMonsters3_Data\StreamingAssets\AB\` (substitui o bundle com o mesmo nome).

## Instalador local de teste

O pacote local privado preparado para o mantenedor usa os arquivos de entrada `Instalar_PTBR.cmd` e `Restaurar_PTBR.cmd`. Os scripts PowerShell e o bundle completo não estão incluídos no repositório público.

O inicializador CMD é o ponto de entrada obrigatório. Ele chama o Windows PowerShell com `-ExecutionPolicy Bypass -STA` somente para aquele processo; não altera a política global de execução do Windows.

## Localização automática do jogo

O instalador usa a variável de ambiente `DQM3_GAME_PATH`.

1. O arquivo `Instalar_PTBR.cmd` define, caso a variável ainda não exista, o caminho padrão:
   `%ProgramFiles(x86)%\Steam\steamapps\common\DRAGON QUEST MONSTERS The Dark Prince`.
2. O instalador valida se esse caminho contém `DQMonsters3.exe`, `DQMonsters3_Data\StreamingAssets\AB` e o bundle esperado da Atualização 13.
3. Se o caminho padrão não for válido, consulta o registro do Steam e os manifestos `appmanifest_2175540.acf` das bibliotecas Steam detectadas, incluindo bibliotecas adicionais.
4. Se localizar uma instalação compatível, usa a pasta automaticamente, sem abrir a janela de seleção.
5. Se não localizar, abre uma janela para o usuário escolher a pasta principal do jogo. A pasta escolhida precisa conter `DQMonsters3.exe`, `DQMonsters3_Data` e o bundle esperado.
6. Depois de validado o caminho, o instalador tenta gravá-lo na variável de ambiente do usuário `DQM3_GAME_PATH`, para as próximas execuções.

Se a variável já estiver definida pelo usuário, o caminho informado tem prioridade, mas ainda precisa passar pelas verificações de compatibilidade.

## Procedimento de teste local

1. Extraia **todo** o pacote local do instalador para uma pasta do Windows. Não execute arquivos diretamente de dentro do ZIP.
2. Feche o jogo.
3. Dê dois cliques em **`Instalar_PTBR.cmd`**. Não execute `Instalar_PTBR.ps1` diretamente.
4. Aguarde a busca automática. Se nenhuma instalação compatível for encontrada, selecione na janela a pasta principal que contém `DQMonsters3.exe` e `DQMonsters3_Data`. Não selecione `StreamingAssets` nem `AB`.
5. Confira o caminho exibido e digite `INSTALAR` para confirmar a substituição.
6. O instalador valida o SHA-256 do bundle, interrompe a instalação se o jogo estiver aberto, faz backup do bundle atual em `Documents\DQM3_PTBR_Backups`, instala o bundle e registra um manifesto.
7. Mantenha o idioma do jogo em **Espanhol**, conforme o LEIA-ME da Atualização 13.
8. Abra o jogo e teste a inicialização, menus, diálogos e os rótulos/conteúdos das três DLCs.

Se a biblioteca estiver protegida e ocorrer erro de acesso, feche o inicializador e execute `Instalar_PTBR.cmd` como administrador. Não altere a política global do PowerShell.

## Restauração

1. Feche o jogo.
2. Dê dois cliques em **`Restaurar_PTBR.cmd`**. Não execute `Restaurar_PTBR.ps1` diretamente.
3. Selecione o `manifest.json` da instalação que deseja reverter.
4. O script verifica o backup e o hash do bundle atual. Se o jogo tiver sido atualizado depois da instalação, a restauração automática é interrompida para evitar sobrescrever dados mais recentes.

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
