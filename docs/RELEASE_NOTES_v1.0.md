# Tradutor PT-BR v1.0 — Notas da versão (patch diferencial)

Primeira versão do tradutor comunitário para português brasileiro de DRAGON QUEST MONSTERS: The Dark Prince para PC/Steam.

## Conteúdo do pacote

- `Instalar_PTBR.cmd` e `Restaurar_PTBR.cmd`.
- `DQM3_PTBR_Installer.exe`, programa auxiliar autônomo Windows x64.
- `patch.json`, com alterações para 331 TextAssets.
- `LEIA-ME.txt` e `SHA256SUMS.txt`.

O pacote não contém o bundle traduzido completo, o executável do jogo ou a estrutura completa da instalação. Python e bibliotecas externas não são necessários.

## Instalação e restauração

O instalador procura a instalação Steam automaticamente e, se necessário, permite selecionar a pasta que contém `DQMonsters3.exe` e `DQMonsters3_Data`. Antes de aplicar a tradução, verifica o SHA-256 do bundle-base. As alterações são aplicadas localmente e a estrutura reconstruída é validada.

O backup original e o manifesto ficam em `Documentos\\DQM3_PTBR_Backups`. Para restaurar, execute `Restaurar_PTBR.cmd`. O restaurador verifica o hash do backup e do bundle atualmente instalado; se o arquivo atual tiver sido alterado depois da instalação, a restauração é interrompida para evitar sobrescrever dados diferentes. Ele reconhece também os manifestos do pacote v1.0 anterior de substituição integral.

Ao iniciar um jogo novo, selecione **Espanhol (Español)**.

## Compatibilidade

- BuildID de referência: `20285966`.
- SHA-256 do bundle-base: `31e716932ab95479be1e1a4b212891f032caefb3fd8dfb39f4d56ae9b115081a`.
- TextAssets modificados: `331`.
- SHA-256 do CAB reconstruído: `56f940a1f1592db59bb964265380eb103b3774dfb01eb2c83aae8d543f9c89a9`.

O executável foi compilado para Windows x64. O candidato precisa de validação funcional em uma instalação real do Windows/Steam antes de ser considerado release público.

## Aviso de direitos e independência

Projeto de fãs, gratuito e não oficial. Não é afiliado, patrocinado, aprovado ou endossado pela Square Enix. O patch contém alterações derivadas da localização do jogo. A distribuição diferencial reduz o conteúdo original incluído, mas não constitui autorização dos titulares nem elimina eventuais questões de direitos autorais. Os direitos sobre o jogo e seus elementos originais permanecem com seus respectivos titulares. O projeto não se apresenta como tradução oficial ou licenciada.
