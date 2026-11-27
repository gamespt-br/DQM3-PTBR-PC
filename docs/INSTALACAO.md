# Instalação — Tradutor PT-BR v1.0 (patch diferencial)

> **Aviso importante:** este é um projeto comunitário, gratuito, independente e não oficial. Não é afiliado, patrocinado, aprovado ou endossado pela Square Enix. Não se apresenta como tradução oficial ou licenciada.
>
> O pacote contém um patch diferencial para aplicar localmente alterações a um arquivo de dados de localização do jogo. Não inclui o bundle traduzido completo, o executável do jogo ou a estrutura completa da instalação. É necessário possuir uma cópia do jogo para PC/Steam.
>
> O patch contém alterações derivadas de recursos de localização do jogo. A distribuição diferencial reduz o conteúdo original incluído no pacote, mas não significa, por si só, autorização dos titulares nem elimina eventuais questões de direitos autorais.

## Conteúdo do ZIP

O pacote contém:
- `Instalar_PTBR.cmd` e `Restaurar_PTBR.cmd`;
- `DQM3_PTBR_Installer.exe`, programa auxiliar Windows x64;
- `patch.json`, com as alterações diferenciais;
- `LEIA-ME.txt` e `SHA256SUMS.txt`.

O ZIP não contém o bundle traduzido completo nem arquivos executáveis do jogo. Python e bibliotecas externas não são necessários.

## Instalar

1. Extraia todo o ZIP para uma pasta do Windows.
2. Feche o jogo.
3. Dê dois cliques em `Instalar_PTBR.cmd`.
4. O instalador tentará localizar o jogo automaticamente pelas configurações e bibliotecas Steam. Se não encontrar, selecione a pasta principal que contém `DQMonsters3.exe` e `DQMonsters3_Data`.
5. Confira o caminho apresentado e digite `INSTALAR` para confirmar.
6. O programa verifica o hash do bundle original, aplica as alterações diferenciais localmente e confere os 331 TextAssets e o CAB reconstruído.
7. Ao iniciar um **jogo novo**, escolha **Espanhol (Español)**. Essa opção é obrigatória para a tradução PT-BR funcionar.

## Backup

Antes de substituir o arquivo, o instalador cria e verifica uma cópia do original em:

`Documentos\\DQM3_PTBR_Backups\\Tradutor_PTBR_v1.0-AAAAmmdd-HHmmss`

O manifesto da instalação fica na mesma pasta. Não apague essa pasta enquanto puder precisar restaurar.

## Restaurar a instalação original

1. Feche o jogo.
2. Dê dois cliques em `Restaurar_PTBR.cmd`.
3. O restaurador procura o manifesto e o backup associados ao caminho da instalação.
4. Confira o arquivo de destino e o backup encontrado.
5. Digite `RESTAURAR` para confirmar.

O backup é verificado pelo SHA-256 antes da restauração. Se o bundle atual não corresponder ao hash registrado como instalado, o processo é interrompido para evitar sobrescrever dados diferentes. O restaurador também reconhece os manifestos do pacote v1.0 anterior que substituía o bundle completo, desde que os backups originais ainda estejam em `Documentos\\DQM3_PTBR_Backups`.

## Compatibilidade e segurança

- Windows 10/11 de 64 bits.
- Bundle original suportado: SHA-256 `31e716932ab95479be1e1a4b212891f032caefb3fd8dfb39f4d56ae9b115081a`.
- BuildID de referência: `20285966`.
- O patch contém 331 registros e valida o CAB reconstruído contra SHA-256 `56f940a1f1592db59bb964265380eb103b3774dfb01eb2c83aae8d543f9c89a9`.
- Se o bundle de origem for diferente, a instalação é interrompida sem substituí-lo.
- Se o bundle instalado tiver sido alterado depois da aplicação, a restauração é interrompida.
- Atualizações futuras do jogo podem exigir uma nova versão.

O programa auxiliar é um executável comunitário sem assinatura digital. O Windows pode exibir um aviso de editor desconhecido. Execute somente se tiver obtido o pacote de uma fonte em que confia. Não desative o Microsoft Defender ou outras proteções do Windows.

## Créditos e independência

DRAGON QUEST MONSTERS: The Dark Prince, seus nomes, personagens, marcas e demais elementos originais pertencem aos respectivos titulares. Eles são mencionados apenas para identificar o jogo compatível. Este projeto é uma iniciativa de fãs, sem associação oficial com a Square Enix e sem reivindicar propriedade sobre os elementos originais.
