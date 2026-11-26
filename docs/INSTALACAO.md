# Instalação — Tradutor PT-BR v1.0

> **Aviso importante:** este é um projeto comunitário, gratuito, independente e não oficial. Não é afiliado, patrocinado, aprovado ou endossado pela Square Enix. Não se apresenta como tradução oficial ou licenciada.
>
> O pacote contém somente **um arquivo de dados de localização do jogo**, modificado para incorporar os textos em português brasileiro, além dos scripts de instalação e restauração. Não inclui o jogo completo, executáveis nem a estrutura completa da instalação. É necessário possuir uma cópia do jogo para PC/Steam.
>
> O arquivo modificado deriva de um recurso original do jogo. A gratuidade e o escopo limitado do pacote não significam, por si só, autorização dos titulares nem eliminam eventuais questões de direitos autorais. Os direitos sobre o jogo e seus elementos originais permanecem com seus respectivos titulares.

## Conteúdo do ZIP

O arquivo `DQM3_PTBR_Tradutor_v1.0.zip` contém:
- `Instalar_PTBR.cmd` e `Instalar_PTBR.ps1`;
- `Restaurar_PTBR.cmd` e `Restaurar_PTBR.ps1`;
- `LEIA-ME.txt`;
- a pasta `bundle`, com somente o arquivo de dados de localização modificado.

## Instalar

1. Extraia todo o ZIP para uma pasta do Windows.
2. Feche o jogo.
3. Dê dois cliques em `Instalar_PTBR.cmd`. Não abra o arquivo `.ps1` diretamente.
4. O instalador tentará localizar o jogo automaticamente. Se não encontrar, selecione a pasta que contém `DQMonsters3.exe` e `DQMonsters3_Data`.
5. Confira o caminho apresentado e digite `INSTALAR` para confirmar.
6. O instalador valida o arquivo esperado e cria e confere o backup original antes da substituição.
7. Ao iniciar um **jogo novo**, escolha **Espanhol (Español)**. Essa opção é obrigatória para a tradução PT-BR funcionar.

## Restaurar a instalação original

1. Feche o jogo.
2. Dê dois cliques em `Restaurar_PTBR.cmd`.
3. O restaurador tentará localizar automaticamente a mesma instalação e o backup correspondente. Se necessário, permite selecionar a pasta do jogo.
4. Se houver mais de um backup compatível, selecione o manifesto correto.
5. Confira o resumo e digite `RESTAURAR` para confirmar.

O backup e o manifesto ficam em `Documentos\\DQM3_PTBR_Backups`. Não os apague enquanto puder precisar restaurar.

## Segurança e compatibilidade

- Não execute instalação ou restauração com o jogo aberto.
- O instalador só aplica a tradução se o arquivo original corresponder ao hash esperado.
- O restaurador confere os hashes antes de substituir o arquivo. Se o arquivo do jogo tiver sido alterado após a instalação, a restauração é interrompida para evitar sobrescrever dados diferentes.
- Atualizações futuras do jogo podem exigir uma nova versão do tradutor.

## Créditos e independência

DRAGON QUEST MONSTERS: The Dark Prince, seus nomes, personagens, marcas e demais elementos originais pertencem aos respectivos titulares. Eles são mencionados apenas para identificar o jogo compatível. Este projeto é uma iniciativa de fãs, sem associação oficial com a Square Enix e sem reivindicar propriedade sobre os elementos originais.
