# OnedriveDownload é um client para fazer download de arquivos do Onedrive

### Requeriments
* python >= 3.7
* onedrivesdk<2

## Primeiro acesso
No primeiro acesso o client vai solicitar a autenticação do usuário na conta do Ondrive, uma vez feito essa autenticação e repassado o "code", o client irá salvar a altenticação no disco.

O client tenta redireionar o retorno do oauth2 para localhost, mas não é necessário ter o serviço no ar, basta copiar o "code" que foi colocado na url de redirect.

## Antes de usar
Antes de usar o client, é necessário configurar a lista de arquivos para download na var *downloadList*.<br>
Se o diretório dos arquivos não for no raiz *root*, também é necessário configurar o *id* do diretório na var *directory_id*   

## Uso
```sh
$ python onedriveDownload.py -l
$ python onedriveDownload.py -d
```


