# ServidorDiretorioPY
Servidor de diretório usando rpc em phyton

## CONST
Nesse arquivo guardamos as constantes com o ip e porta do servidor de diretórios 
## CLIENT
Nesse arquivo temos o códgio do cliente que vai fazer a conexão com servidor de diretório e fazer requisição através do servidor de diretório para buscar o servirdor desejado
## SERVER
Nesse arquivo temos o servidor do qual o cliente estará "procurando", nele iremos iniciar o servidor de diretório e posteriormente iremos registrar este servidor no servidor de diretório
## SERVERDIR
Nesse arquivo temos o servidor de diretório que tem as funções de registrar servidor, que recebe um serverName, ip e porta e registra ele. E temos a função que buscaServer que recebe um sereverName e realiza a busca verificando se o server está registrado. Este é o servidor que intercala a conexão entre o client e o server que ele deseja se conectar.
