# Tradutor PT-BR v1.0 — Dragon Quest Monsters: The Dark Prince (PC)

Primeira versão do tradutor comunitário para português brasileiro da versão PC/Steam testada pelo responsável do projeto.

> **Projeto independente, gratuito e não oficial.** Não é afiliado, patrocinado, aprovado ou endossado pela Square Enix. Não possuímos autorização ou licença oficial da Square Enix para esta tradução ou para a distribuição do arquivo de dados modificado.

## Aviso sobre conteúdo e direitos

O pacote contém **um único arquivo de dados de localização do jogo**, modificado para incorporar textos em português brasileiro, além dos scripts auxiliares de instalação e restauração.

Este pacote **não contém o jogo completo, o executável do jogo nem a estrutura completa de instalação**. É necessário possuir sua própria cópia de DRAGON QUEST MONSTERS: The Dark Prince para PC/Steam.

O arquivo de localização é um recurso técnico derivado do jogo e mantém a estrutura necessária para ser lido por ele. Portanto, não é um arquivo independente de legendas criado do zero. Os direitos sobre o jogo e seus elementos originais permanecem com seus respectivos titulares.

A tradução é disponibilizada gratuitamente e sem finalidade comercial. **A gratuidade, o escopo limitado a um único arquivo e este aviso de independência não significam autorização dos titulares nem eliminam, por si só, eventuais questões de direitos autorais.** O projeto não deve ser confundido com uma tradução oficial ou licenciada. O responsável reavaliará a disponibilização diante de eventual solicitação dos titulares dos direitos.

## Download

Quando publicada, a versão **Tradutor PT-BR v1.0** ficará na página [Releases](https://github.com/gamespt-br/DQM3-PTBR-PC/releases).

O pacote `DQM3_PTBR_Tradutor_v1.0.zip` contém:
- `Instalar_PTBR.cmd` e `Instalar_PTBR.ps1`;
- `Restaurar_PTBR.cmd` e `Restaurar_PTBR.ps1`;
- `LEIA-ME.txt`;
- uma pasta `bundle` com somente o arquivo de dados de localização modificado.

Não será distribuída uma cópia do jogo, seu executável ou sua estrutura completa de instalação. O ZIP do pacote não é armazenado no histórico Git do repositório.

## Como instalar

1. Baixe e extraia `DQM3_PTBR_Tradutor_v1.0.zip` para uma pasta.
2. Feche o jogo.
3. Execute `Instalar_PTBR.cmd`. Não abra o arquivo `.ps1` diretamente.
4. O instalador tentará localizar o jogo automaticamente. Se não encontrar, selecione a pasta que contém `DQMonsters3.exe` e `DQMonsters3_Data`.
5. Confira o caminho apresentado e digite `INSTALAR` para confirmar. O instalador cria e verifica um backup antes de substituir o arquivo.
6. Ao iniciar um **jogo novo**, escolha **Espanhol (Español)** na tela de idioma. Essa escolha é obrigatória para a tradução funcionar.

O backup original e o manifesto ficam em `Documentos\\DQM3_PTBR_Backups`. Não apague esses arquivos enquanto puder precisar restaurar a instalação.

## Restaurar a instalação original

1. Feche o jogo.
2. Execute `Restaurar_PTBR.cmd`.
3. O restaurador tentará localizar a instalação e o backup correspondente automaticamente. Se necessário, permite selecionar a pasta do jogo ou o manifesto.
4. Confira o resumo e digite `RESTAURAR` para confirmar.

O restaurador confere os hashes do backup e do arquivo instalado. Se o arquivo atual tiver sido alterado depois da instalação — por exemplo, por uma atualização do jogo — a restauração é interrompida para evitar sobrescrever dados diferentes.

## Imagens do jogo traduzido

### Tutorial de combate
![Tutorial de combate em português](screenshots/01_tutorial_combate.jpg)

### Informações do monstro
![Informações do monstro em português](screenshots/02_informacoes_do_monstro.jpg)

### Diálogo com Moncho
![Diálogo com Moncho em português](screenshots/03_dialogo_moncho.jpg)

### Diálogo com Gaureen
![Diálogo com Gaureen em português](screenshots/04_dialogo_gaureen.jpg)

### Diálogo da campanha
![Diálogo da campanha em português](screenshots/05_dialogo_mestre_dos_monstros.jpg)

### Menu de grupo
![Menu de grupo em português](screenshots/06_menu_grupo_e_tutorial.jpg)

### Diálogo com Royston
![Diálogo com Royston em português](screenshots/07_dialogo_royston.jpg)

## Compatibilidade

Esta primeira versão foi preparada para a versão de PC testada pelo responsável do projeto. Atualizações futuras do jogo podem exigir uma nova versão do tradutor. Não force a instalação em arquivos diferentes dos esperados pelo instalador.

## Créditos

DRAGON QUEST MONSTERS: The Dark Prince é uma obra de seus respectivos titulares. Os nomes, marcas e elementos originais são mencionados apenas para identificar o jogo compatível com este projeto comunitário.
