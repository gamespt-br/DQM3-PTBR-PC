# Instalação — Tradutor PT-BR v1.0

> **Aviso importante:** este é um projeto comunitário, gratuito, independente e não oficial. Não é afiliado, patrocinado, aprovado ou endossado pela Square Enix. Não se apresenta como tradução oficial ou licenciada.
>
> O pacote contém somente **um arquivo de dados de localização do jogo**, modificado para incorporar os textos em português brasileiro. Não inclui o jogo completo, executáveis nem a estrutura completa da instalação. É necessário possuir uma cópia do jogo para PC/Steam.
>
> O arquivo modificado deriva de um recurso original do jogo. A gratuidade e o escopo limitado do pacote não significam, por si só, autorização dos titulares nem eliminam eventuais questões de direitos autorais. Os direitos sobre o jogo e seus elementos originais permanecem com seus respectivos titulares.

## Instalar

1. Extraia todo o conteúdo do ZIP para uma pasta do Windows.
2. Feche o jogo.
3. Dê dois cliques em **`Instalar_PTBR.cmd`**. Não execute o arquivo `.ps1` diretamente.
4. O instalador procura o jogo automaticamente. Se não encontrar, abre uma janela para selecionar a pasta que contém `DQMonsters3.exe` e `DQMonsters3_Data`.
5. Confira o caminho e digite **`INSTALAR`**.
6. Aguarde a confirmação de conclusão.

## Idioma obrigatório

Ao iniciar um **jogo novo**, o jogo pede que você escolha um idioma. Selecione **Espanhol (Español)**. A tradução PT-BR depende dessa opção para funcionar corretamente.

## Restaurar a instalação original

1. Feche o jogo.
2. Dê dois cliques em **`Restaurar_PTBR.cmd`**.
3. O restaurador procura o jogo automaticamente pelo mesmo caminho salvo usado na instalação, pelo caminho padrão e pelas bibliotecas Steam.
4. Se não encontrar o jogo, abre uma janela para você selecionar a pasta que contém `DQMonsters3.exe` e `DQMonsters3_Data`.
5. Depois de localizar o jogo, procura o backup correspondente àquela instalação. Se houver mais de um backup possível, permite escolher o manifesto correto.
6. Confira o resumo e digite **`RESTAURAR`** para confirmar.

## Importante

- Use sempre os arquivos `.cmd` para instalar e restaurar. Eles executam o PowerShell com uma autorização temporária, sem alterar a política de segurança do Windows.
- A instalação e a restauração usam a variável de ambiente `DQM3_GAME_PATH` para lembrar o local do jogo.
- O backup fica em `Documentos\\DQM3_PTBR_Backups`. Não o apague enquanto puder precisar restaurar.
- O restaurador verifica os arquivos de backup e o bundle instalado antes de substituir qualquer coisa. Se detectar uma alteração posterior ou atualização do jogo, interrompe a restauração para evitar sobrescrever dados mais recentes.
- Se o jogo estiver em execução, feche-o antes de instalar ou restaurar.
- Esta é a primeira versão do tradutor (**v1.0**). Uma atualização futura do jogo pode exigir uma nova versão.

## Créditos e independência

DRAGON QUEST MONSTERS: The Dark Prince, seus nomes, personagens, marcas e demais elementos originais pertencem aos respectivos titulares. Eles são mencionados apenas para identificar o jogo compatível. Este projeto é uma iniciativa de fãs, sem associação oficial com a Square Enix. Não reivindicamos propriedade sobre o jogo ou seus elementos originais.
